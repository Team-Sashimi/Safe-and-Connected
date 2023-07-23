# Generated by Django 4.2.3 on 2023-07-22 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0019_rename_client_organizationmembership_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientlanguagemembership',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='event_attendees',
            field=models.ManyToManyField(related_name='attending', to=settings.AUTH_USER_MODEL),
        ),
    ]