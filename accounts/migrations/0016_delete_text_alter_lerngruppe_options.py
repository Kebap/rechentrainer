# Generated by Django 4.0 on 2022-12-19 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='text',
        ),
        migrations.AlterModelOptions(
            name='lerngruppe',
            options={'verbose_name_plural': 'Lerngruppen'},
        ),
    ]
