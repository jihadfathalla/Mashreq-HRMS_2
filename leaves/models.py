from django.db import models
from employees.models import *
from datetime import datetime

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
    resume_date = models.DateField()
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
        days = (self.end_date - self.start_date)
        return (days.days)
 
    
    def get_leave_value_of_type(leave_type):
        leave_type = LeaveMaster.objects.get(id=leave_type)
        return leave_type.leave_value

    def  if_em_in_leave(emp_id):
        emp_leaves = EmployeeLeave.objects.filter(emp_id = emp_id)
        if  len(emp_leaves) == 0: 
            return False
        else:
            emp_last_leave = emp_leaves.order_by('-id')[0]
            if emp_last_leave.start_date < datetime.now().date() and emp_last_leave.resume_date > datetime.now().date():
                return True
            else:
                return False


    def is_leave_balance_valid(emp_id ,leave_value,start_date,end_date):
        emp = CustomUser.objects.get(id = emp_id)
        emp_leaves_balance = emp.balance
        requested_leave_period =  end_date - start_date
        requested_leave_value = requested_leave_period.days * leave_value
        if emp_leaves_balance >= requested_leave_value:
            return True
        else:
            return False

        

    def __str__(self):
        return self.emp_id.username
    