from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название поста', max_length=1000)
    address = models.CharField('Адрес', max_length=2000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/post/{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
