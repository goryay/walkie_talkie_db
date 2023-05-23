from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Accounting
from .forms import AccountingForm
from django.db.models import Q


@login_required
def accounting_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        accounts = Accounting.objects.filter(
            Q(id__icontains=search_query) | Q(id_walkie_talkie__serial_number__icontains=search_query) | Q(
                id_post__name__icontains=search_query) | Q(id_organization__name__icontains=search_query) | Q(
                id_resposible__resposible_fio__icontains=search_query))
    else:
        accounts = Accounting.objects.all()
    return render(request, "accounting/list.html", {'accounts': accounts})


@login_required
def accounting_create(request):
    if request.method == "POST":
        form = AccountingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(accounting_list)
            except:
                pass
    else:
        form = AccountingForm()
    return render(request, 'accounting/create.html', {'form': form})


@login_required
def accounting_update(request, id):
    accounting = Accounting.objects.get(id=id)
    form = AccountingForm(initial={'id_walkie_talkie': accounting.id_walkie_talkie,
                                   'id_organization': accounting.id_organization,
                                   'id_resposible': accounting.id_resposible,
                                   'id_post': accounting.id_post,
                                   'id_state': accounting.id_state,
                                   'relevance': accounting.relevance,
                                   'document': accounting.document,
                                   'date': format(accounting.date, '%Y-%m-%dT%H:%M'),
                                   'comments': accounting.comments
                                   })
    if request.method == "POST":
        form = AccountingForm(request.POST, instance=accounting)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(accounting_list)
            except Exception as e:
                pass
    return render(request, 'accounting/update.html', {'form': form})


@login_required
def accounting_delete(request, id):
    accounting = Accounting.objects.get(id=id)
    try:
        accounting.delete()
    except:
        pass
    return redirect(accounting_list)
