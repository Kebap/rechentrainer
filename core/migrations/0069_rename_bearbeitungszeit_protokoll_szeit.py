# Generated by Django 4.0 on 2023-01-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_rename_bearbeitungszeit_zaehler_zeit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protokoll',
            old_name='bearbeitungszeit',
            new_name='szeit',
        ),
    ]
