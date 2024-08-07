from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=23)
    email = models.EmailField()
    gender = models.CharField(max_length=23)
    salary = models.FloatField()