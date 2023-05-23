from django.forms import ModelForm, TextInput
from .models import Organization


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
