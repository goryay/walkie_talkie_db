# Generated by Django 4.1.4 on 2023-01-09 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='id_organization',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='organization',
            old_name='organization_name',
            new_name='name',
        ),
    ]