from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import WalkieTalkie
from .forms import WalkieTalkieForm
from django.db.models import Q


@login_required
def walkie_talkie_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        walkie_talkies = WalkieTalkie.objects.filter(
            Q(id__icontains=search_query) | Q(serial_number__icontains=search_query) | Q(
                id_organization__name__icontains=search_query) | Q(wt_name__icontains=search_query))
    else:
        walkie_talkies = WalkieTalkie.objects.all()
    return render(request, "walkie_talkie/list.html", {'walkie_talkies': walkie_talkies})


@login_required
def walkie_talkie_create(request):
    if request.method == "POST":
        form = WalkieTalkieForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(walkie_talkie_list)
            except:
                pass
    else:
        form = WalkieTalkieForm()
    return render(request, 'walkie_talkie/create.html', {'form': form})


@login_required
def walkie_talkie_update(request, id):
    walkie_talkie = WalkieTalkie.objects.get(id=id)
    form = WalkieTalkieForm(initial={
        'id_organization': walkie_talkie.id_organization,
        'serial_number': walkie_talkie.serial_number,
        'frequency': walkie_talkie.frequency,
        'permission': walkie_talkie.permission,
        'callsing': walkie_talkie.callsing,
        'certificate_number': walkie_talkie.certificate_number,
        'date_of_purchase': format(walkie_talkie.date_of_purchase, '%Y-%m-%dT%H:%M'),
        'date_of_received': format(walkie_talkie.date_of_received, '%Y-%m-%dT%H:%M'),
        'use_of_RES': walkie_talkie.use_of_RES,
    })
    if request.method == "POST":
        form = WalkieTalkieForm(request.POST, instance=walkie_talkie)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(walkie_talkie_list)
            except Exception as e:
                pass
    return render(request, 'walkie_talkie/update.html', {'form': form})


@login_required
def walkie_talkie_delete(request, id):
    walkie_talkie = WalkieTalkie.objects.get(id=id)
    try:
        walkie_talkie.delete()
    except:
        pass
    return redirect(walkie_talkie_list)
