# Generated by Django 4.0.3 on 2022-05-27 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_schueler_e_kurs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaehler',
            name='optionen',
        ),
        migrations.RemoveField(
            model_name='zaehler',
            name='stufe_next',
        ),
        migrations.RemoveField(
            model_name='zaehler',
            name='stufe_zaehl',
        ),
        migrations.AddField(
            model_name='zaehler',
            name='bearbeitungszeit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='zaehler',
            name='message',
            field=models.CharField(blank=True, max_length=40, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='zaehler',
            name='optionen_text',
            field=models.CharField(blank=True, max_length=40, verbose_name='Optionen'),
        ),
    ]
