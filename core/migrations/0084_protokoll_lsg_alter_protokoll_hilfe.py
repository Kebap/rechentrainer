# Generated by Django 4.1.5 on 2023-02-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_protokoll_abbrechen'),
    ]

    operations = [
        migrations.AddField(
            model_name='protokoll',
            name='lsg',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='protokoll',
            name='hilfe',
            field=models.BooleanField(default=False),
        ),
    ]
