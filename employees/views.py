from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate,  update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_permission
from rolepermissions.roles import get_user_roles
from .decorators import allowed_users
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile/profile.html')


@allowed_users(allowed_roles=['admin'])
def signupPage(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            subject = 'welcome to GFG world'
            message = 'Hi {username.username}, thank you for registering .'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [user.email, ] 
            send_mail( subject, message, email_from, recipient_list ) 
        return HttpResponseRedirect('/employees/')
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/employees')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/employees/profile/')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/employees/login/')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def employees_list(request):
    all_employees = CustomUser.objects.all()
    context = {'all_employees': all_employees}
    return render(request, 'employee/employees_list.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_employee(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            assign_role(user, 'user')
            form.save()
            return HttpResponseRedirect('/employees/')
    return render(request, 'employee/create_employee.html', {'form': form})

@login_required(login_url='login')
def employee_detail(request, num):
    em = CustomUser.objects.get(id=num)
    context = {'em': em}
    return render(request, 'employee/employee_detail.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_employee(request, num):
    em = CustomUser.objects.get(id=num)
    context = {'em': em}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, instance=em)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/employees/')
    else:
        form = CustomUserCreationForm(instance=em)
    return render(request, 'employee/edit_employee.html', {'form': form})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_employee(request, num):
    em = CustomUser.objects.get(id=num)
    em.delete()
    return HttpResponseRedirect('employees/')
