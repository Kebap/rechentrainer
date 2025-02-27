# Generated by Django 4.0 on 2023-03-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_rename_lfd_nr_hilfe_hilfe_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sachaufgabe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lfd_nr', models.SmallIntegerField(default=0, unique=True)),
                ('ab_jg', models.SmallIntegerField(default=0)),
                ('text', models.TextField()),
                ('loesung', models.JSONField()),
                ('pro_text', models.CharField(max_length=25)),
                ('links_text', models.CharField(max_length=25)),
                ('ergebnis', models.DecimalField(decimal_places=2, max_digits=7)),
                ('rechts_text', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'Sachaufgaben',
            },
        ),
    ]
