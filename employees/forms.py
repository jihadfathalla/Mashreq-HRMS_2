from django import forms
from employees.models import *
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User




class DateInput(forms.DateInput):
	input_type = 'date'	 


		
class CustomUserCreationForm(UserCreationForm): 
    class Meta:
        model = CustomUser
        widget = {
            "date_of_birth":DateInput(),
            "hire_date":DateInput(),
        }
        fields = UserCreationForm.Meta.fields+(
		'email',
        'gender',
		'address',
		'nationality',
		'id_type',
		'id_num',
		'hire_date',
		'social_status',
		'emp_unm',
		'date_of_birth',
		'place_of_birth',
		'mobile_num',
		'insured',
		'is_active',
		'has_medical',
		'balance',
		'manager',
        )
        


		
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        widget = {
            "date_of_birth":DateInput(),
            "hire_date":DateInput(),
        }
        fields = (
        'username',
        'email',
        'gender',
		'address',
		'nationality',
		'id_type',
		'id_num',
		'hire_date',
		'social_status',
		'emp_unm',
		'date_of_birth',
		'place_of_birth',
		'mobile_num',
		'insured',
		'is_active',
		'has_medical',
		'balance',
		'manager',
        )

     