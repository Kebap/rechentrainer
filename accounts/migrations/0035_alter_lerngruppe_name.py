# Generated by Django 4.0 on 2023-01-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_alter_profil_lerngruppe_alter_profil_ort_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lerngruppe',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
