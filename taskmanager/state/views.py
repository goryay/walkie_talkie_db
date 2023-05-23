from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import State
from .forms import StateForm


@login_required
def state_list(request):
    states = State.objects.all()
    return render(request, "state/list.html", {'states': states})


@login_required
def state_create(request):
    if request.method == "POST":
        form = StateForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(state_list)
            except:
                pass
    else:
        form = StateForm()
    return render(request, 'state/create.html', {'form': form})


@login_required
def state_update(request, id):
    state = State.objects.get(id=id)
    form = StateForm(initial={'name': state.name})
    if request.method == "POST":
        form = StateForm(request.POST, instance=state)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(state_list)
            except Exception as e:
                pass
    return render(request, 'state/update.html', {'form': form})


@login_required
def state_delete(request, id):
    state = State.objects.get(id=id)
    try:
        state.delete()
    except:
        pass
    return redirect(state_list)
