from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from leaves.models import *
from employees.models import *
from leaves.forms import *
from django.contrib import messages
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail

def leaves_list(request):
    all_leaves = LeaveMaster.objects.all()
    context = {'all_leaves': all_leaves}
    return render(request, 'leave/leaves_list.html', context)


def create_leave(request):
    form = leaveForm()
    if request.method == "POST":
        form = leaveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves/')
    return render(request, 'leave/create_leave.html', {'form': form})


def leave_detail(request, num):
    le = LeaveMaster.objects.get(id=num)
    context = {'le': le}
    return render(request, 'leave/leave_detail.html', context)


def edit_leave(request, num):
    le = LeaveMaster.objects.get(id=num)
    context = {'le': le}
    if request.method == "POST":
        form = leaveForm(request.POST, instance=le)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves/')
    else:
        form = leaveForm(instance=le)
    return render(request, 'leave/edit_leave.html', {'form': form})


def delete_leave(request, num):
    le = LeaveMaster.objects.get(id=num)
    le.delete()
    return HttpResponseRedirect('/leaves/')


def employee_leave_list(request):
    all_leaves_requests = EmployeeLeave.objects.all()
    context = {'all_leaves_requests': all_leaves_requests}
    return render(request, 'employee_leaves/employee_leaves_list.html', context)


def create_employee_leave(request):
    form = EmployeeLeaveForm()
    if request.method == "POST":
        form = EmployeeLeaveForm(request.POST)
        emp_id = form.data['emp_id']
        leave_type = form.data['leave_id']
        start_date = datetime.strptime(form.data['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(form.data['end_date'], '%Y-%m-%d')
        leave_value = EmployeeLeave.get_leave_value_of_type(leave_type)
        
        if form.is_valid():
            if EmployeeLeave.if_em_in_leave(emp_id) == False:
                if EmployeeLeave.is_leave_balance_valid(emp_id,leave_value,start_date,end_date)== True:
                    emp = CustomUser.objects.get(id = emp_id)
                    leave_type_obj = LeaveMaster.objects.get(id = leave_type)
                    subject = 'welcome to Mashreq Arabia HR'
                    message = f'''Hi sir,Please review Mr {emp.username} leave request.
                    Leave Start Date: {start_date}.
                    Leave End Date: {end_date}.
                    Leave Type: {leave_type_obj.leave_name}.
                    Employee Available Balance:{emp.balance}'''
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [emp.manager.email ] 
                    send_mail( subject, message, email_from, recipient_list )

                    form.save()
                    return HttpResponseRedirect('/leaves/employee_leaves')
                else:
                    messages.error(request , 'You do not have enough balance for this leave')
            else:
                messages.error(request, 'You cant ask for a new leave while you are in another leave')
    return render(request , 'employee_leaves/create_employee_leave.html' , {'form':form})


def employee_leave_detail(request, num):
    le = EmployeeLeave.objects.get(id=num)
    context = {'le': le}
    return render(request, 'employee_leaves/employee_leave_detail.html', context)


def edit_employee_leave(request, num):
    le = EmployeeLeave.objects.get(id=num)
    context = {'le': le}
    if request.method == "POST":
        form = EmployeeLeaveForm(request.POST, instance=le)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/leaves/employee_leaves')
    else:
        form = EmployeeLeaveForm(instance=le)
    return render(request, 'employee_leaves/edit_employee_leave.html', {'form': form})


def delete_employee_leave(request, num):
    le = EmployeeLeave.objects.get(id=num)
    le.delete()
    return HttpResponseRedirect('/leaves/employee_leaves')



def change_emp_balance(emp_id , leave_type , start_date , end_date):
    emp = CustomUser.objects.filter(id = emp_id)
    leave_value = EmployeeLeave.get_leave_value_of_type(leave_type)
    requested_leave_period =  end_date - start_date
    requested_leave_value = requested_leave_period.days * leave_value
    leave_balance = emp[0].balance - requested_leave_value
    emp.update(balance = leave_balance)
    return emp[0].balance    

def approved(request, num):
    leave= EmployeeLeave.objects.filter(id=num)
    new_balance = change_emp_balance(leave[0].emp_id.id , leave[0].leave_id.id , leave[0].start_date , leave[0].end_date)
    leave.update(confirm = "Approved")
    messages.success(request, 'Leave Approved!')    
    emp = CustomUser.objects.get(id = leave[0].emp_id.id)
    subject = 'Your Leave Request'
    message = f'''Hi {emp.username}, We want to inform you that your leave request has been approaved.'''
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [emp.email] 
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/leaves/employee_leaves')



def not_approved(request, num):
    leave = EmployeeLeave.objects.filter(id=num)
    leave.update(confirm = "Not approved")
    emp = CustomUser.objects.get(id = leave[0].emp_id.id)
    subject = 'Your Leave Request'
    message = f'''Hi {emp.username}, We want to inform you that your leave request has been rejected.'''
    email_from = settings.EMAIL_HOST_USER 
    recipient_list =  [emp.email] 
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('/leaves/employee_leaves/')



