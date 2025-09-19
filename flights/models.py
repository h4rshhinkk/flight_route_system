from django.db import models

# Create your models here.

# class Airport(models.Model):
#     code = models.CharField(max_length=10, unique=True)
#     position = models.CharField(max_length=100)  # City / name
#     def __str__(self):
#         return self.code


# class Route(models.Model):
#     source = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
#     destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
#     duration = models.PositiveIntegerField(help_text="Duration in minutes")

#     def __str__(self):
#         return f"{self.source.code} → {self.destination.code} ({self.duration} min)"


class AirportNode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    position = models.CharField(max_length=100)

    # Left and right children (self-referential for binary tree)
    left = models.ForeignKey(
        "self", null=True, blank=True,
        related_name="left_parent", on_delete=models.SET_NULL
    )
    right = models.ForeignKey(
        "self", null=True, blank=True,
        related_name="right_parent", on_delete=models.SET_NULL
    )
    # Duration from the parent node to this node (minutes)
    duration = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.code