# Generated by Django 4.2.3 on 2023-07-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0032_alter_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_language',
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('es', 'es'), ('fr', 'fr'), ('sw', 'sw'), ('en', 'en')], default='en', max_length=5),
        ),
    ]
