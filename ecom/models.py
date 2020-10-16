from django.db import models

# Create your models here.
class Medicine(models.Model):

    Medicine_Name = models.CharField(max_length=255)
    Price = models.IntegerField()
    Medicine_Type = models.CharField(max_length=255)
    About_it = models.CharField(max_length=255)
    Medicine_image = models.CharField(max_length=255)