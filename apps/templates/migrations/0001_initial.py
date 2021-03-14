# Generated by Django 3.1.4 on 2021-03-14 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('kind', models.CharField(choices=[('Issue', 'Issue'), ('Investigation', 'Investigation')], max_length=13)),
                ('title', models.CharField(max_length=50)),
                ('json', models.JSONField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('presentation', models.TextField(blank=True, null=True)),
                ('hints', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='template_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Templates',
                'ordering': ['-title'],
                'unique_together': {('title', 'kind', 'json')},
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.TextField(blank=True, null=True)),
                ('json', models.JSONField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('differential', models.TextField(blank=True, null=True)),
                ('presentation', models.TextField(blank=True, null=True)),
                ('conclusion', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue_templates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Issues',
                'ordering': ['-title'],
                'unique_together': {('title', 'json')},
            },
        ),
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.TextField(blank=True, null=True)),
                ('json', models.JSONField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='investigation_templates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Investigations',
                'ordering': ['-title'],
                'unique_together': {('title', 'json')},
            },
        ),
    ]
