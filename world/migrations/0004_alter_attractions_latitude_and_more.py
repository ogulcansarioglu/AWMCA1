# Generated by Django 4.2.6 on 2023-11-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0003_attractions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractions',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='attractions',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
