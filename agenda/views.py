from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from agenda.models import  Timetable, Scheduling
from products.models import Order, ProductModel
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')

def agendar(request):
    
    prodmodels = get_list_or_404(ProductModel)
    timetable = get_list_or_404(Timetable)
    users = User.objects.filter(groups__name='attendant')
    print(users.query)
    
    params = {
        'prodmodels': prodmodels,
        'timetable': timetable,
        'attendants': users
    }
    
    return render(request, 'agendar/form.html', params)

def registrar_agendamento(request):
    
    if Scheduling.objects.filter(date=request.POST['date'], hour=request.POST['timetable']).exists():
        return render(request, 'agendar/form.html', {'error': 'Horário indisponível'})
    
    new_scheduling = Scheduling()
    new_scheduling.date = request.POST['date']
    new_scheduling.hour = request.POST['timetable']
    new_scheduling.description = request.POST['description']
    new_scheduling.client = request.POST['client']
    new_scheduling.order = get_object_or_404(Order, pk=request.POST['order'])
    new_scheduling.attendant = get_object_or_404(User, username=request.POST['attendant'])
    new_scheduling.save()
    
    return redirect('/agendar/')
    