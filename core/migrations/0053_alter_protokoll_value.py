# Generated by Django 4.0 on 2022-10-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_hilfe_kategorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protokoll',
            name='value',
            field=models.DecimalField(decimal_places=7, max_digits=20, null=True, verbose_name='Wert'),
        ),
    ]
