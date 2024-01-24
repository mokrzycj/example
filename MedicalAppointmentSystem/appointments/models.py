# models.py w aplikacji appointments

from django.db import models
from profiles.models import Profile

class Availability(models.Model):
    specialist = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.specialist} dostępny od {self.start_time} do {self.end_time}"

class Appointment(models.Model):
    patient = models.ForeignKey(Profile, related_name='appointments', on_delete=models.CASCADE)
    specialist = models.ForeignKey(Profile, related_name='appointments_as_specialist', on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('scheduled', 'Scheduled'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Wizyta {self.patient} z {self.specialist} na {self.scheduled_time}"
