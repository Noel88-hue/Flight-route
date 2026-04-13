from django.db import models

from django.db import models

class AirportRoute(models.Model):
    airport_code = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.airport_code} ({self.position})"