# Generated by Django 3.0.5 on 2020-11-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='Nmae',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='Paaword',
            new_name='Password',
        ),
        migrations.AlterField(
            model_name='car',
            name='Phone',
            field=models.IntegerField(),
        ),
    ]