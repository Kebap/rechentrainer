# Generated by Django 4.0.3 on 2022-10-12 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_alter_protokoll_user_alter_zaehler_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protokoll',
            name='halbjahr',
        ),
    ]
