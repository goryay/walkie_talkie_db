# Generated by Django 4.1.4 on 2023-01-09 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resposible', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposible',
            old_name='id_resposible',
            new_name='id',
        ),
    ]
