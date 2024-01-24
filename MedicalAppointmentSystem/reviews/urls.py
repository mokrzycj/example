# urls.py w aplikacji reviews

from django.urls import path
from .views import add_review, review_list

urlpatterns = [
    path('add/', add_review, name='add_review'),
    path('list/', review_list, name='review_list'),
]
