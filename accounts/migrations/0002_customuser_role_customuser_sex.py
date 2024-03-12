# Generated by Django 4.2.7 on 2023-11-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('student', 'Student'), ('instructor', 'Instructor'), ('admininstrator', 'Administrator')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=10, null=True),
        ),
       
    ]
