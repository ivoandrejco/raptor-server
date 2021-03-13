# Generated by Django 3.1.4 on 2021-02-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0008_investigation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investigation',
            options={'ordering': ['-title'], 'verbose_name_plural': 'Investigations'},
        ),
        migrations.AddField(
            model_name='investigation',
            name='slug',
            field=models.TextField(blank=True, null=True),
        ),
    ]
