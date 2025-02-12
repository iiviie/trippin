# Generated by Django 5.0.10 on 2025-02-05 14:09

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trip', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BucketListItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('priority', models.CharField(choices=[('HIGH', 'High Priority'), ('MEDIUM', 'Medium Priority'), ('LOW', 'Low Priority')], default='MEDIUM', max_length=10)),
                ('status', models.CharField(choices=[('PENDING', 'Not Started'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='PENDING', max_length=20)),
                ('target_date', models.DateField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('associated_trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bucket_list_items', to='trip.trip')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bucket_list_items', to='trip.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucket_list_items', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['priority', '-created_at'],
                'indexes': [models.Index(fields=['user'], name='bucket_list_user_id_b36868_idx'), models.Index(fields=['priority'], name='bucket_list_priorit_74eea4_idx'), models.Index(fields=['status'], name='bucket_list_status_ea4d74_idx')],
            },
        ),
    ]
