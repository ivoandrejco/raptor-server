# Generated by Django 3.1.4 on 2021-02-03 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-updated_on', '-created_on']},
        ),
    ]
