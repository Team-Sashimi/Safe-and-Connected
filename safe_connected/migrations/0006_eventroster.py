# Generated by Django 4.2.3 on 2023-07-18 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0005_alter_event_event_language_alter_event_event_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safe_connected.event')),
            ],
        ),
    ]