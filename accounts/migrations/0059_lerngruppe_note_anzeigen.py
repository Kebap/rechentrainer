# Generated by Django 4.0 on 2024-01-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0058_profil_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='lerngruppe',
            name='note_anzeigen',
            field=models.BooleanField(default=True),
        ),
    ]
