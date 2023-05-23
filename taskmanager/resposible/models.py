from django.db import models
from department.models import Department


class Resposible(models.Model):
    id = models.AutoField(primary_key=True)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resposible_fio = models.CharField('ФИО ответственного', max_length=600)

    def __str__(self):
        return self.resposible_fio

    def get_absolute_url(self):
        return f'/resposible/{self.id}'

    class Meta:
        verbose_name = 'Ответственный'
        verbose_name_plural = 'Ответственные'
