# Generated by Django 3.1.4 on 2021-03-24 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consultations', '0003_auto_20210323_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('BMI', models.FloatField(blank=True, null=True)),
                ('IBW', models.FloatField(blank=True, null=True, verbose_name='Ideal Body Weight')),
                ('ABW', models.FloatField(blank=True, null=True, verbose_name='Adjusted Body Weight')),
                ('BSA_D', models.FloatField(blank=True, null=True, verbose_name='Body Surface Area(Dubois)')),
                ('BSA_M', models.FloatField(blank=True, null=True, verbose_name='Body Surface Area(Mosteller)')),
                ('pulse', models.IntegerField(blank=True, null=True)),
                ('pulse_desc', models.CharField(blank=True, max_length=8, null=True, verbose_name='Pulse Description')),
                ('BP', models.CharField(blank=True, max_length=8, null=True, verbose_name='Blood Pressure')),
                ('temp', models.FloatField(blank=True, null=True)),
                ('sats', models.IntegerField(blank=True, null=True)),
                ('findings', models.TextField(blank=True, null=True, verbose_name='Findings')),
                ('collected_on', models.DateField()),
                ('updated_on', models.DateField()),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examinations', to='consultations.consultation', verbose_name='Consultation')),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='examination_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Examinations',
                'ordering': ['-collected_on'],
                'unique_together': {('consultation', 'collected_on')},
            },
        ),
    ]
