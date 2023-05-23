from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Department


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
