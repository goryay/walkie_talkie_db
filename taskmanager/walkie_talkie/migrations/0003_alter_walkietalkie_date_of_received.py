# Generated by Django 4.1.4 on 2023-01-09 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walkie_talkie', '0002_rename_id_walkie_talkie_walkietalkie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walkietalkie',
            name='date_of_received',
            field=models.DateField(verbose_name='Дата выдачи'),
        ),
    ]
