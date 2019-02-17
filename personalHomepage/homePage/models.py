from django.db import models

# Create your models here.
class Travel(models.Model):
    location_x = models.FloatField()
    location_y = models.FloatField()
    text = models.CharField(max_length=1000)