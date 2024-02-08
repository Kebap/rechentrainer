# Generated by Django 4.0 on 2022-10-20 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_hilfe'),
    ]

    operations = [
        migrations.AddField(
            model_name='hilfe',
            name='kategorie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hilfe', to='core.kategorie'),
            preserve_default=False,
        ),
    ]
