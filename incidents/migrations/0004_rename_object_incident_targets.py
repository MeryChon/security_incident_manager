# Generated by Django 4.1.2 on 2022-10-24 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0003_remove_commonvulnerabilityexposure_incidents_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='object',
            new_name='targets',
        ),
    ]