# forms.py w aplikacji reviews

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['reviewed', 'rating', 'comment']
