# Generated by Django 4.0 on 2022-12-19 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_delete_text_alter_lerngruppe_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ort',
            old_name='postleitzahl',
            new_name='plz',
        ),
    ]
