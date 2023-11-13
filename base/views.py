from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .forms import employeeForm, positionForm
from .models import Employee

# Create your views here.

def employee_list(request): #Read
    context = {'employee_list' : Employee.objects.all()}
    return render(request, 'employee_list.html',context)

def employee_form(request, id=0): #Create & Update
    
    if request.method == "GET":
        if id == 0:
            form = employeeForm()
        else:
            employee = Employee.objects.get(pk = id)
            form = employeeForm(instance= employee)
        # position_form = positionForm()
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id == 0:
            form = employeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = employeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('list')

def employee_delete(request, id): #Delete
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('list')

def employee_edit(request, id):

    pass