from django import forms
from .models import Department, Employee
from django.core.exceptions import ValidationError
from dal import autocomplete

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

class EmployeeAutocompleteForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name']

        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
        }
