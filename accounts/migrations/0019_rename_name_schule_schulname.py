# Generated by Django 4.0 on 2022-12-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_lehrer_kurs_alter_lerngruppe_lehrer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schule',
            old_name='name',
            new_name='schulname',
        ),
    ]
