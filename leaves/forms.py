from django import forms
from leaves.models import *
from employees.models import *
from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'


class leaveForm(forms.ModelForm):
    class Meta:
        model = LeaveMaster
        fields = "__all__"

 
class EmployeeLeaveForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeave
        fields = "__all__"
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'resume_date' : DateInput(),
        }

    def check_leave_is_end(self, user_id):
        today = date.today()
        last_leave = EmployeeLeave.objects.filter(emp_id=user_id).reverse()
        if len(last_leave) > 0:
            if(today < last_leave[0].end_date):
                print(last_leave[0].emp_id)
                return False
            else:
            	print("true")
            	return True
        return True
