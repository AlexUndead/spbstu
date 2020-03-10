from django.urls import path

from .views import *

urlpatterns = [
    path('employees/', employees, name='employees'),
    path('autocomplete/', EmployeesAutocomplete.as_view(), name='autocomplete'),
    path('employees/<int:id>/', employees_profile, name='employee_profile'),
    path('employees/update/<int:emp_id>/del_department/<int:dep_id>/', department_delete, name='department_delete'),
    path('departments/', departments, name='departments'),
    path('departments/create/', DepartmentsCreate.as_view(), name='departments_create'),
    path('departments/update/<int:dep_id>/add_employee/<int:emp_id>/', add_employee, name='add_employee'),
    path('departments/update/<int:id>/', DepartmentsUpdate.as_view(), name='departments_update'),
    path('departments/<int:id>/', departments_profile, name='department_profile'),
    path('', index, name='index'),
]
