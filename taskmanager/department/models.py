from django.db import models


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название отдела', max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/department/{self.id}'

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
