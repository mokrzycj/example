# urls.py w aplikacji clinics

from django.urls import path
from .views import clinic_list, clinic_detail, new_clinic_request

urlpatterns = [
    path('list/', clinic_list, name='clinic_list'),
    path('detail/<int:clinic_id>/', clinic_detail, name='clinic_detail'),
    path('new-request/<int:clinic_id>/', new_clinic_request, name='new_clinic_request'),
]
