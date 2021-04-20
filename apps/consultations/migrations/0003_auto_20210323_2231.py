# Generated by Django 3.1.4 on 2021-03-23 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultations', '0002_auto_20210314_2323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='issue',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='tid',
        ),
        migrations.DeleteModel(
            name='Investigation',
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]