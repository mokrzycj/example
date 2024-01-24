# urls.py w aplikacji appointments

from django.urls import path
from .views import schedule_appointment, cancel_appointment

urlpatterns = [
    path('schedule/', schedule_appointment, name='schedule_appointment'),
    path('cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
]
