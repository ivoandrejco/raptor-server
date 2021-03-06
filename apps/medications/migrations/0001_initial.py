# Generated by Django 3.1.4 on 2021-01-19 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('dose', models.CharField(blank=True, max_length=50, null=True)),
                ('frequency', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('ceased', models.BooleanField(default=False)),
                ('ceased_on', models.DateField(blank=True, null=True)),
                ('reviewed_on', models.DateField()),
                ('created_on', models.DateField()),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='medications_created_by', to=settings.AUTH_USER_MODEL)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='patients.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name_plural': 'Medications',
                'ordering': ['-name'],
                'unique_together': {('pid', 'name', 'created_on')},
            },
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('drug', models.CharField(max_length=50)),
                ('reaction', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='allergies_created_by', to=settings.AUTH_USER_MODEL)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergies', to='patients.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name_plural': 'Allergies',
                'ordering': ['-drug'],
                'unique_together': {('pid', 'drug')},
            },
        ),
    ]
