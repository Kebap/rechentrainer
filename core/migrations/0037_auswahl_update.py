# Generated by Django 4.0 on 2022-08-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_kategorie_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='auswahl',
            name='update',
            field=models.BooleanField(default=True),
        ),
    ]
