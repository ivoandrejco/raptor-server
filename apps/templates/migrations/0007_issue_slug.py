# Generated by Django 3.1.4 on 2021-02-13 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0006_auto_20210206_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='slug',
            field=models.TextField(blank=True, null=True),
        ),
    ]
