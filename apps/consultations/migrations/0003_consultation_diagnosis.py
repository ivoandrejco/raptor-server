# Generated by Django 3.1.4 on 2021-02-25 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0001_initial'),
        ('consultations', '0002_investigation_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='diagnosis',
            field=models.ForeignKey(default='bdf011f5-cff4-480f-abbd-d8c43984beda', on_delete=django.db.models.deletion.CASCADE, related_name='diagnosis_consultations', to='diagnoses.diagnosis', verbose_name='Diagnosis'),
            preserve_default=False,
        ),
    ]
