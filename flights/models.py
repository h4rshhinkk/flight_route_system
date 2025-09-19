from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=100)  # City / name
    def __str__(self):
        return self.code


class Route(models.Model):
    source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.source.code} → {self.destination.code} ({self.duration} min)"