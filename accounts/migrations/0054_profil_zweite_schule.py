# Generated by Django 4.0.3 on 2023-09-14 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_alter_profil_jg_alter_profil_schule'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='zweite_schule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schule2', to='accounts.schule'),
        ),
    ]
