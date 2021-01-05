# accounts/urls.py
from django.urls import path
from employees import views


urlpatterns = [
    path('employees/signup/', views.signupPage),
    path('employees/login/', views.loginPage),
    path('employees/logout/', views.logoutPage),
    path('employees/profile/', views.profile),



    path('employees/', views.employees_list),
    path('employees/add/', views.create_employee),
    path('employees/<num>/', views.employee_detail),
    path('employees/edit/<num>/', views.edit_employee),
    path('employees/delete/<num>/', views.delete_employee),



]