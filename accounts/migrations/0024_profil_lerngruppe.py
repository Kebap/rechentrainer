# Generated by Django 4.0 on 2022-12-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_lerngruppe'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='lerngruppe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.lerngruppe'),
        ),
    ]
