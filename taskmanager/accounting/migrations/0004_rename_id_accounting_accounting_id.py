# Generated by Django 4.1.4 on 2023-01-09 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_alter_accounting_id_accounting'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounting',
            old_name='id_accounting',
            new_name='id',
        ),
    ]
