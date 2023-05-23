from django.forms import ModelForm, DateInput
from walkie_talkie.models import WalkieTalkie


class WalkieTalkieForm(ModelForm):

    class Meta:
        model = WalkieTalkie
        fields = '__all__'
        labels = {'id_organization': 'Название организации'}

        widgets = {
            'date_of_purchase': DateInput(
                format='%d-%m-%Y',
                attrs={'type': 'datetime-local'
                       }),
            'date_of_received': DateInput(
                format='%d-%m-%Y',
                attrs={'type': 'datetime-local'
                       }),
        }
