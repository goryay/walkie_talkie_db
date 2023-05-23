from django.forms import ModelForm, DateInput, Textarea, CheckboxInput
from accounting.models import Accounting


class AccountingForm(ModelForm):
    class Meta:
        model = Accounting
        fields = '__all__'

        labels = {
                    'id_walkie_talkie': 'Серийный номер рации',
                    'id_organization': 'Название организации',
                    'id_resposible': 'Арендодатель',
                    'id_post': 'Название поста',
                    'id_state': 'Cостояние',
        }
        widgets = {
            "relevance": CheckboxInput(),
            "comments": Textarea(),
            'date': DateInput(
                format='%d-%m-%Y%H:%M',
                attrs={'type': 'datetime-local'
                       }),
        }
