from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.specialization}"
