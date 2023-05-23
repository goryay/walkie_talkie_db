from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact, Task
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ContactForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['first_name', 'last_name', 'email', 'message', ]
        widgets = {
            'message': Textarea(attrs={
                'placeholder': 'Напишите тут ваше сообщение.'
            })
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task

        fields = ['title', 'task']
        widgets = {
            'message': Textarea(attrs={
                'placeholder': 'Напишите тут ваше задание.'
            })
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']