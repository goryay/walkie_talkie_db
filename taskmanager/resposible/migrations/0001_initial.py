# Generated by Django 4.1.4 on 2023-01-08 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposible',
            fields=[
                ('id_resposible', models.AutoField(primary_key=True, serialize=False)),
                ('resposible_fio', models.CharField(max_length=600, verbose_name='ФИО ответственного')),
                ('id_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department')),
            ],
            options={
                'verbose_name': 'Ответственный',
                'verbose_name_plural': 'Ответственные',
            },
        ),
    ]
