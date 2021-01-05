from django.db import models
from employees.models import *
from datetime import timedelta
# Create your models here.


class LeaveMaster(models.Model): 
    leave_name = models.CharField(max_length=33)
    leave_value = models.IntegerField()

    def __str__(self):
        return self.leave_name


class EmployeeLeave(models.Model):
    CONFIRM_CHOICE = (
        ('Approved', 'Approved'),
        ('Waiting for apprave', 'Waiting for apprave'),
        ('Not approved', 'Not approved')
    )
    emp_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    leave_id = models.ForeignKey(LeaveMaster, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirm = models.CharField(
        max_length=60,
        choices=CONFIRM_CHOICE,
        default = 'Waiting for apprave',
        blank=True,
        null=True,
    )

    leave_reasons = models.TextField(
        blank=True,
        null=True,
    )

    def calculate_number_of_days(self):
        return (self.end_date - self.start_date).days

    def calculate_resume_date(self):
        return self.end_date + timedelta(self.calculate_number_of_days())

         

    def __str__(self):
        return self.emp_id
    