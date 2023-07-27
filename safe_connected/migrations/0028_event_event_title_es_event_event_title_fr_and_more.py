# Generated by Django 4.2.3 on 2023-07-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safe_connected', '0027_remove_event_event_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_title_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_title_fr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='general_notes_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='general_notes_fr',
            field=models.TextField(null=True),
        ),
    ]