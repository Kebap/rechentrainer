# Generated by Django 4.0 on 2022-06-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_protokoll_falsch_eingabe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protokoll',
            name='hilfe',
            field=models.TextField(blank=True),
        ),
    ]
