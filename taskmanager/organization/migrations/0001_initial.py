# Generated by Django 4.1.4 on 2023-01-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id_organization', models.AutoField(primary_key=True, serialize=False)),
                ('organization_name', models.CharField(max_length=5000, verbose_name='Название организации')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организация',
            },
        ),
    ]
