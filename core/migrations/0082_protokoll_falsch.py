# Generated by Django 4.1.5 on 2023-02-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_remove_protokoll_abbrechen_remove_protokoll_falsch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='protokoll',
            name='falsch',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
