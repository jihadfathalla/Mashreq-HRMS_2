from django import forms
from contracts.models import *



class DateInput(forms.DateInput):
		input_type = 'date'	
 

class ContractForm(forms.ModelForm):
	class Meta:
		model = Contract
		widgets = {
            "start_date":DateInput(),
            "end_date":DateInput(),
        }
		fields = (
		'user_id',	
		'dep_id',
		'pos_id',
		'start_date',
		'end_date',
		) 


class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = (
		'department_name',
		'department_dec',
		) 


class PositionForm(forms.ModelForm):
	class Meta:
		model = Position
		fields = (
		'position_name',
		) 	


