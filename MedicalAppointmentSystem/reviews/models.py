# models.py w aplikacji reviews

from django.db import models
from profiles.models import Profile

class Review(models.Model):
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='given_reviews')
    reviewed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    response = models.TextField(blank=True)

    def __str__(self):
        return f"Opinia od {self.reviewer} dla {self.reviewed}"
