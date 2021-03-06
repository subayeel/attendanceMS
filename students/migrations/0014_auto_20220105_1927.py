# Generated by Django 3.2.8 on 2022-01-05 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_studentinfo_att_percent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='att_percent',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_lab1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_lab2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub4',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub5',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='att_percent_sub6',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
