# Generated by Django 3.1.4 on 2021-04-03 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schema',
            unique_together={('title', 'kind')},
        ),
    ]