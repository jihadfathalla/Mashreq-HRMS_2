from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from contracts.models import *
from employees.models import CustomUser
from .forms import ContractForm, DepartmentForm, PositionForm



# Create your views here.

def contracts_list(request):
	all_contracts = Contract.objects.all()
	context = {'all_contracts':all_contracts }
	return render(request ,'contract/contracts_list.html' , context)

def create_contract(request):
	form = ContractForm()
	if request.method == "POST":
		form = ContractForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/')
	return render(request, 'contract/create_contract.html', {'form':form})

def contract_detail (request, num):
	em=Contract.objects.get(id=num) 
	context={'em': em}
	return render(request ,'contract/contract_detail.html' , context)

def edit_contract(request,num):
	em =  Contract.objects.get(id=num)
	context={'em': em}
	if request.method == "POST":
		form = ContractForm( request.POST, instance=em)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/')
	else:
			form = ContractForm( instance=em)
	return render(request, 'contract/edit_contract.html', {'form':form})


def delete_contract(request, num):
	em = Contract.objects.get(id = num)
	em.delete()
	return HttpResponseRedirect('/contracts/')		




def departments_list(request): 
	all_departments = Department.objects.all()
	context = {'all_departments':all_departments }
	return render(request ,'department/departments_list.html' , context)

def create_department(request):
	form = DepartmentForm()
	if request.method == "POST":
		form = DepartmentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/departments')
	return render(request, 'department/create_department.html', {'form':form})


def department_detail (request, num):
	de=Department.objects.get(id=num)
	context={'de': de}
	return render(request ,'department/department_detail.html' , context)


def edit_department(request,num):
	de =  Department.objects.get(id=num)
	context={'de': de}
	if request.method == "POST":
		form = DepartmentForm( request.POST, instance=de)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/departments')
	else:
			form = DepartmentForm( instance=de)
	return render(request, 'department/edit_department.html', {'form':form})

def delete_department(request, num):
	de = Department.objects.get(id = num)
	de.delete()
	return HttpResponseRedirect('/contracts/departments')		



def positions_list(request): 
	all_positions = Position.objects.all()
	context = {'all_positions':all_positions }
	return render(request ,'position/positions_list.html' , context)


def create_position(request):
	form = PositionForm()
	if request.method == "POST":
		form = PositionForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/positions')
	return render(request, 'position/create_position.html', {'form':form})



def position_detail (request, num):
	po=Position.objects.get(id=num)
	context={'po': po}
	return render(request ,'position/position_detail.html' , context)



def edit_position(request,num):
	po = Position.objects.get(id=num)
	context={'po': po}
	if request.method == "POST":
		form = PositionForm( request.POST, instance=po)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contracts/positions')
	else:
			form = PositionForm( instance=po)
	return render(request, 'position/edit_position.html', {'form':form})


def delete_position(request, num):
	po = Position.objects.get(id = num)
	po.delete()
	return HttpResponseRedirect('/contracts/positions')		




