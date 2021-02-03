from django.db import models
from ..people.models import Employee

class Appointment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    availability = models.DateTimeField()

