# Generated by Django 4.0 on 2023-01-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_alter_profil_voreinst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='voreinst',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
