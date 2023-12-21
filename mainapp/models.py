
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    tenure = models.IntegerField()
    hire_date = models.DateField()

