# Generated by Django 4.0 on 2024-01-15 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0059_lerngruppe_note_anzeigen'),
    ]

    operations = [
        migrations.AddField(
            model_name='lerngruppe',
            name='ab',
            field=models.DateField(auto_now_add=True, default=datetime.date(2023, 8, 1)),
            preserve_default=False,
        ),
    ]
