# Generated by Django 3.0.5 on 2020-11-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20201119_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='Phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
