# Generated by Django 4.2.7 on 2023-11-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapi', '0003_doctor_tags_alter_doctor_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish'), ('de', 'German'), ('it', 'Italian'), ('pt', 'Portuguese'), ('nl', 'Dutch'), ('ru', 'Russian'), ('zh', 'Chinese'), ('ja', 'Japanese'), ('ko', 'Korean'), ('ar', 'Arabic'), ('hi', 'Hindi'), ('bn', 'Bengali'), ('ur', 'Urdu'), ('tr', 'Turkish'), ('sv', 'Swedish'), ('da', 'Danish'), ('no', 'Norwegian'), ('fi', 'Finnish')], max_length=50),
        ),
    ]