# Generated by Django 3.2.6 on 2021-08-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ns_parcelbox_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='humidity_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temp',
            field=models.IntegerField(),
        ),
    ]
