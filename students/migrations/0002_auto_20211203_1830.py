# Generated by Django 3.2.8 on 2021-12-03 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='sub1_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sub2_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sub3_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sub4_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sub5_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='sub6_att',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='lab1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab1', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='lab2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab2', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub1', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub2', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub3', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub4', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub5', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='sub6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub6', to='students.studentsubjectinfo'),
        ),
    ]
