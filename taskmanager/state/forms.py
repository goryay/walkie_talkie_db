from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import State


class StateForm(ModelForm):
    class Meta:
        model = State
        fields = '__all__'
