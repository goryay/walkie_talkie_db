from django.db import models


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Состояние', max_length=380)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/state/{self.id}'

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'
