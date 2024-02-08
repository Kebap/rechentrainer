# Generated by Django 4.0 on 2023-02-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_alter_hilfe_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protokoll',
            old_name='parameter',
            new_name='variable',
        ),
        migrations.AlterField(
            model_name='kategorie',
            name='farbe',
            field=models.CharField(choices=[('background-color: #B0E2FF', 'Gruppe A'), ('background-color: #9AFF9A', 'Gruppe B'), ('background-color: #FFFACD', 'Gruppe C'), ('background-color: #FFDEAD', 'Gruppe D'), ('background-color: #FFB5C5', 'Gruppe E')], max_length=25),
        ),
    ]
