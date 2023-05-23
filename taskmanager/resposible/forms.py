from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from resposible.models import Resposible


class ResposibleForm(ModelForm):
    class Meta:
        model = Resposible
        fields = '__all__'
        labels = {"id_department": "Департамент"}
