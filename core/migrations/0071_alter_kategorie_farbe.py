# Generated by Django 4.0 on 2023-01-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_kategorie_farbe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategorie',
            name='farbe',
            field=models.CharField(choices=[('background-color: #B0E2FF', 'Gruppe A'), ('background-color: #9AFF9A', 'Gruppe B')], max_length=25),
        ),
    ]
