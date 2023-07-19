# Generated by Django 4.2.3 on 2023-07-19 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0009_alter_organizationprofile_org_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventroster',
            name='event_manager',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventroster',
            name='event_organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='safe_connected.organizationprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventroster',
            name='client_attendee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safe_connected.clientprofile'),
        ),
    ]
