# Generated by Django 3.2.6 on 2021-08-06 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Humidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity_level', models.IntegerField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='TimeGenerated')),
            ],
        ),
        migrations.CreateModel(
            name='Motion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motion', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='TimeGenerated')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.IntegerField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='TimeGenerated')),
            ],
        ),
    ]