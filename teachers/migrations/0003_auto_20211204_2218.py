# Generated by Django 3.2.8 on 2021-12-04 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_studentsubjectinfo_professor_name'),
        ('teachers', '0002_auto_20211204_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='sub1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psub1', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='sub2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psub2', to='students.studentsubjectinfo'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='sub3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='psub3', to='students.studentsubjectinfo'),
        ),
    ]
