# Generated by Django 3.2.9 on 2021-12-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20211207_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='lab1_att',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='lab2_att',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
