# Generated by Django 4.0 on 2022-09-30 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
