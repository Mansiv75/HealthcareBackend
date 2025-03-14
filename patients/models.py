from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Patient creator
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    disease = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
