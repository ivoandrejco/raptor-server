# Generated by Django 3.1.4 on 2021-02-26 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnosis',
            old_name='dtype',
            new_name='kind',
        ),
    ]
