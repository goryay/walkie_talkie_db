from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Organization
from .forms import OrganizationForm


@login_required
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, "organization/list.html", {'organizations': organizations})


@login_required
def organization_create(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(organization_list)
            except:
                pass
    else:
        form = OrganizationForm()
    return render(request, 'organization/create.html', {'form': form})


@login_required
def organization_update(request, id):
    organization = Organization.objects.get(id=id)
    form = OrganizationForm(initial={'name': organization.name})
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(organization_list)
            except Exception as e:
                pass
    return render(request, 'organization/update.html', {'form': form})


@login_required
def organization_delete(request, id):
    organization = Organization.objects.get(id=id)
    try:
        organization.delete()
    except:
        pass
    return redirect(organization_list)
