# Generated by Django 4.1.4 on 2023-01-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_alter_accounting_id_accounting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounting',
            name='id_accounting',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
