from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee


def dashboard(request):
    employees = Employee.objects.all().order_by('-id')

    context = {
        'employees': employees,
        'total_employees': employees.count(),
    }

    return render(request, 'employees/dashboard.html', context)


def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            designation=request.POST.get('designation'),
            salary=request.POST.get('salary'),
        )
        return redirect('dashboard')

    return render(request, 'employees/employee_form.html')


def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.designation = request.POST.get('designation')
        employee.salary = request.POST.get('salary')
        employee.save()

        return redirect('dashboard')

    return render(request, 'employees/employee_form.html', {
        'employee': employee
    })


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        employee.delete()

    return redirect('dashboard')