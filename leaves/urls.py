from django.urls import path
from leaves import views
urlpatterns = [
    path('leaves/', views.leaves_list),
    path('leaves/employee_leaves/', views.employee_leave_list),

    path('leaves/add/', views.create_leave),
    path('leaves/employee_leaves/add/', views.create_employee_leave),

    path('leaves/<num>/', views.leave_detail),
    path('leaves/employee_leaves/<num>/', views.employee_leave_detail),


    path('leaves/edit/<num>/', views.edit_leave),
    path('leaves/employee_leaves/edit/<num>/', views.edit_employee_leave),

    path('leaves/delete/<num>/', views.delete_leave),
    path('leaves/employee_leaves/delete/<num>/', views.delete_employee_leave),


    path('leaves/<num>/approved',views.approved),
    path('leaves/<num>/not_approved',views.not_approved),

    
]








