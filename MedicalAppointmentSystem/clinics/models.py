# models.py w aplikacji clinics

from django.db import models
from profiles.models import Profile

class Clinic(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    # Dodatkowe pola

    def __str__(self):
        return self.name

class ClinicRequest(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('accepted', 'Accepted')])

    def __str__(self):
        return f"Wniosek {self.specialist} do {self.clinic}"
