from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Employee, Department
from .forms import DepartmentForm, EmployeeAutocompleteForm
from django.http import Http404
from django.views.generic import View
from dal import autocomplete
from django.db.models import Q

def index(request):
    return render(request, 'index.html', context={})

def employees(request):
    employees = Employee.objects.all
    return render(request, 'employees.html', context={'employees':employees})

def employees_profile(request, id):
    profile = get_object_or_404(Employee, id=id)
    return render(request, 'employee_profile.html', context={
        'department':profile.department,
        'full_name':'{} {}'.format(profile.first_name, profile.last_name),
        'age':profile.age,
        'description':profile.description,
    })

class EmployeesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Employee.objects.all()

        if self.q:
            qs = qs.filter(
                Q(first_name__istartswith=self.q)|
                Q(last_name__istartswith=self.q)|
                Q(age__istartswith=self.q)|
                Q(city__name__istartswith=self.q)|
                Q(department__name__istartswith=self.q)
            )

        return qs

def add_employee(request, dep_id, emp_id):
    employee = Employee.objects.filter(id=emp_id).update(department_id=dep_id)
    return redirect('departments_update', dep_id)

def department_delete(request, emp_id, dep_id):
    employee = Employee.objects.filter(id=emp_id).update(department=None)
    return redirect('departments_update', dep_id)

class DepartmentsCreate(View):
    template = 'departments_create.html'

    def get(self, request):
        form = DepartmentForm()

        return render(request, self.template, context={
            'form':form,
        })

    def post(self, request):
        bound_form = DepartmentForm(request.POST)

        if bound_form.is_valid():
            new_department = bound_form.save()
            return redirect('department_profile', new_department.id)
        return render(request, self.template, context={
            'form':bound_form,
        })

class DepartmentsUpdate(View):
    template = 'departments_update.html'

    def get_department(self, id):
        return get_object_or_404(Department, id=id)

    def get(self, request, id):
        department = self.get_department(id)
        form = DepartmentForm(instance=department)
        autocomplete_form = EmployeeAutocompleteForm()

        return render(request, self.template, context={
            'department':department,
            'form':form,
            'autocomplete_form':autocomplete_form,
        })

    def post(self, request, id):
        department = self.get_department(id)
        bound_form = DepartmentForm(request.POST, instance=department)

        if bound_form.is_valid():
            update_department = bound_form.save()
            return redirect('department_profile', update_department.id)
        return render(request, self.template, context={
            'form':bound_form,
        })


def departments(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', context={'departments':departments})

def departments_profile(request, id):
    profile = get_object_or_404(Department, id=id)
    return render(request, 'department_profile.html', context={'department_profile':profile})
