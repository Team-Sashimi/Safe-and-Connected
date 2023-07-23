# Generated by Django 4.2.3 on 2023-07-23 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0021_alter_event_event_attendees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_attendees',
            field=models.ManyToManyField(blank=True, null=True, related_name='attended_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safe_connected.organizationprofile'),
        ),
    ]
