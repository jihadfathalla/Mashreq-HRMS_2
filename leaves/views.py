from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from leaves.models import *
from leaves.forms import *
from django.contrib import messages
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.messages import constants


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
        if form.is_valid():
            check_date = form.check_leave_is_end(request.user.id)
            if check_date == True:
                leave = form.save(commit=False)
                leave.emp_id = request.user
                leave.save()
            else:
                messages.error(request, 'You are in a Leave Now')

        return HttpResponseRedirect('/leaves/employee_leaves')
    return render(request, 'employee_leaves/create_employee_leave.html', {'form': form})


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



def approved(request, num):
    EmployeeLeave.objects.filter(id=num).update(confirm='Approved')
    messages.success(request, 'Leave Approved!')
    return HttpResponseRedirect('/leaves/employee_leaves/')

def not_approved(request, num):
    EmployeeLeave.objects.filter(id=num).update(confirm='Not approved')
    messages.error(request, 'Leave Not approved!')
    return HttpResponseRedirect('/leaves/employee_leaves/')

