# Generated by Django 5.0 on 2024-03-11 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_role_customuser_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
    ]