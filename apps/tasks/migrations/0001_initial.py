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
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=9)),
                ('updated_on', models.DateField()),
                ('created_on', models.DateField()),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks_created_by', to=settings.AUTH_USER_MODEL)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_pid', to='patients.patient', verbose_name='Patient')),
            ],
            options={
                'ordering': ['-status', '-created_on'],
                'unique_together': {('pid', 'name', 'created_on')},
            },
        ),
    ]
