# Generated by Django 4.2.3 on 2023-07-21 19:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0017_managerorgmembership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmembership',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
