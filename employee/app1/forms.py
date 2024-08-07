from django import forms
from .models import Employee

gen = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        labels = {
            'id' : 'Employee ID',
            'name' : 'Employee Name',
            'email' : 'E-mail',
            'gender' : 'Gender',
            'salary' : 'Salary',
        }

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(choices=gen),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
        }