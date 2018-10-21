from django.db import models

# Create your models here.
class Sensor(models.Model):
    value = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.value