# Generated by Django 4.0.3 on 2022-10-13 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_lehrer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schueler',
            name='halbjahr',
        ),
        migrations.AddField(
            model_name='schueler',
            name='hj',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schueler',
            name='sj',
            field=models.SmallIntegerField(default=0),
        ),
    ]
