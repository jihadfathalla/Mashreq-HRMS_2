from django.urls import path
from contracts import views
urlpatterns = [
    path('contracts/', views.contracts_list),
    path('contracts/departments/', views.departments_list),
    path('contracts/positions/', views.positions_list),

    path('contracts/add/', views.create_contract),
    path('contracts/departments/add/', views.create_department),
    path('contracts/positions/add/', views.create_position),

    path('contracts/<num>/', views.contract_detail),
    path('contracts/departments/<num>/', views.department_detail),
    path('contracts/positions/<num>/', views.position_detail),

    path('contracts/edit/<num>/', views.edit_contract),
    path('contracts/departments/edit/<num>/', views.edit_department),
    path('contracts/positions/edit/<num>/', views.edit_position),

    path('contracts/delete/<num>/', views.delete_contract),
    path('contracts/departments/delete/<num>/', views.delete_department),
    path('contracts/positions/delete/<num>/', views.delete_position),

   
    
]
