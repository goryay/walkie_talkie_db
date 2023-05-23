from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Department
from .forms import DepartmentForm


@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, "department/list.html", {'departments': departments})


@login_required
def department_create(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(department_list)
            except:
                pass
    else:
        form = DepartmentForm()
    return render(request, 'department/create.html', {'form': form})


@login_required
def department_update(request, id):
    department = Department.objects.get(id=id)
    form = DepartmentForm(initial={'name': department.name})
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(department_list)
            except Exception as e:
                pass
    return render(request, 'department/update.html', {'form': form})


@login_required
def department_delete(request, id):
    department = Department.objects.get(id=id)
    try:
        department.delete()
    except:
        pass
    return redirect(department_list)
