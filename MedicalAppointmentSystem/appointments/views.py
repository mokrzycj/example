# views.py w aplikacji appointments

from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.profile
            appointment.save()
            return redirect('appointments_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})

def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.status = 'cancelled'
    appointment.save()
    return redirect('appointments_list')
