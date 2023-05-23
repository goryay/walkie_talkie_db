# Generated by Django 4.1.4 on 2023-01-12 07:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('walkie_talkie', '0005_walkietalkie_date_of_purchase_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='walkietalkie',
            name='wt_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=1200, verbose_name='Наименование'),
            preserve_default=False,
        ),
    ]
