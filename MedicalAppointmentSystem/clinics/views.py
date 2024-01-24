# views.py w aplikacji clinics

from django.shortcuts import render, redirect
from .forms import ClinicForm, ClinicRequestForm
from .models import Clinic, ClinicRequest

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinics/clinic_list.html', {'clinics': clinics})

def clinic_detail(request, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})

def new_clinic_request(request, clinic_id):
    if request.method == 'POST':
        form = ClinicRequestForm(request.POST)
        if form.is_valid():
            clinic_request = form.save(commit=False)
            clinic_request.clinic_id = clinic_id
            clinic_request.specialist = request.user.profile
            clinic_request.save()
            return redirect('clinic_list')
    else:
        form = ClinicRequestForm()
    return render(request, 'clinics/new_clinic_request.html', {'form': form})
