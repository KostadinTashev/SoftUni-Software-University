from django.shortcuts import render, get_object_or_404, redirect

from models_demo.web.models import Employee, Department


def index(request):
    # Employee.objects.get(level=Employee.LEVEL_SENIOR)
    # get_object_or_404(Employee, level=Employee.LEVEL_JUNIOR)
    # print(Employee.objects.filter(level=Employee.LEVEL_JUNIOR).first())
    employees = Employee.objects.all()
    # employees2 = Employee.objects.filter(department_id=2) \
    #     .order_by('last_name', 'first_name')
    employees2 = Employee.objects \
        .filter(age__gte=10) \
        .order_by('last_name', 'first_name')
    department = Department.objects.get(pk=2)

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }
    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }
    return render(request, 'department-details.html', context)


def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('index')
