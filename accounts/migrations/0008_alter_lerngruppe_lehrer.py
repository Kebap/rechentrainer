# Generated by Django 4.0.3 on 2022-10-11 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_schueler_lerngruppe_alter_lehrer_schule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lerngruppe',
            name='lehrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.lehrer'),
        ),
    ]
