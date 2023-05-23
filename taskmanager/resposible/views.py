from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Resposible
from .forms import ResposibleForm


@login_required
def resposible_list(request):
    resposibles = Resposible.objects.all()
    return render(request, "resposible/list.html", {'resposibles': resposibles})


@login_required
def resposible_create(request):
    if request.method == "POST":
        form = ResposibleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(resposible_list)
            except:
                pass
    else:
        form = ResposibleForm()
    return render(request, 'resposible/create.html', {'form': form})


@login_required
def resposible_update(request, id):
    resposible = Resposible.objects.get(id=id)
    form = ResposibleForm(initial={'resposible_fio': resposible.resposible_fio})
    if request.method == "POST":
        form = ResposibleForm(request.POST, instance=resposible)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect(resposible_list)
            except Exception as e:
                pass
    return render(request, 'resposible/update.html', {'form': form})


@login_required
def resposible_delete(request, id):
    resposible = Resposible.objects.get(id=id)
    try:
        resposible.delete()
    except:
        pass
    return redirect(resposible_list)
