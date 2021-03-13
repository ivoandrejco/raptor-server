# Generated by Django 3.1.4 on 2021-01-19 21:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]