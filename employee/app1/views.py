from django.shortcuts import render
from django.views  import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'app1/home.html', {})

class StudentCreateView(CreateView):
    template_name = 'app1/form.html'
    form_class = EmployeeForm
    success_url = '/a1/sv/'

class StudentListView(ListView):
    template_name = 'app1/show.html'
    model = Employee
    context_object_name = 'obj'

class StudentUpdateView(UpdateView):
    template_name = 'app1/form.html'
    form_class = EmployeeForm
    model = Employee
    success_url = '/a1/sv/'

class StudentDeleteView(DeleteView):
    template_name = 'app1/success.html'
    model = Employee
    context_object_name = 'obj'
    success_url = '/a1/sv/'
