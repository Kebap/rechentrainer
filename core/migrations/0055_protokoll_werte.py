# Generated by Django 4.0 on 2022-10-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_alter_protokoll_hilfe'),
    ]

    operations = [
        migrations.AddField(
            model_name='protokoll',
            name='werte',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
