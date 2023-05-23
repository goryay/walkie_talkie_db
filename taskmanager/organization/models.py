from django.db import models


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название организации', max_length=5000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/organization/{self.id}'

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организация'

