from django.db import models
from ..people.models import Employee

class Appointment(models.Model):
    date = models.DateTimeField()

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    availability = models.DateTimeField()

    def __str__(self):
        return f"""
        Appointment confirmd for \
        {self.date.strftime('%B %d, %y, %I:%M %P')} \
        with {self.employee,__str__()}
        """

    

