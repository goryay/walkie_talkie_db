from django.db import models
from organization.models import Organization


class WalkieTalkie(models.Model):
    id = models.AutoField(primary_key=True)
    id_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    wt_name = models.CharField('Наименование', max_length=1200)
    serial_number = models.CharField('Серийный номер', max_length=1200)
    frequency = models.CharField('Номинальнал частоты р/частоты (МГц)', max_length=500)
    permission = models.CharField('Разрешение', max_length=1200)
    callsing = models.CharField('Позывной', max_length=500)
    certificate_number = models.CharField('Номер свидетельства', max_length=500)
    date_of_purchase = models.DateTimeField('Дата покупки')
    date_of_received = models.DateTimeField('Дата выдачи (ввод в эксплуатацию)')
    use_of_RES = models.CharField('Использование РЭС', max_length=20)

    def __str__(self):
        return self.serial_number

    def get_absolute_url(self):
        return f'/walkie_talkie/{self.id}'

    class Meta:
        verbose_name = 'Рация'
        verbose_name_plural = 'Рации'
