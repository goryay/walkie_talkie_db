from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
from .forms import UserRegisterForm


def index(request):
    # task = Task.object.all()
    data = {
        'title': 'Home',
    }
    # return render(request, 'main/index.html', data, {'task': task})
    return render(request, 'main/index.html', data)


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'main/profile.html')