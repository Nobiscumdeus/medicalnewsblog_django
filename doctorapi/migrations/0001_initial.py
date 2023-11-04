# Generated by Django 4.2.6 on 2023-10-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'Prefer not to say')], max_length=1)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('education', models.TextField()),
                ('address', models.TextField()),
                ('town', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=9)),
                ('working_hours', models.TextField()),
                ('bio', models.TextField()),
                ('awards_and_recognitions', models.TextField()),
                ('years_of_experience', models.PositiveIntegerField()),
                ('is_board_certified', models.BooleanField(default=False)),
                ('license_number', models.CharField(max_length=20, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('available_for_consultation', models.BooleanField(default=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapi.country')),
                ('hospital_affiliations', models.ManyToManyField(to='doctorapi.hospital')),
                ('insurance_company', models.ManyToManyField(to='doctorapi.insurancecompany')),
                ('languages_spoken', models.ManyToManyField(to='doctorapi.language')),
                ('medical_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapi.medicalschool')),
                ('publications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapi.publication')),
                ('specialization', models.ManyToManyField(to='doctorapi.specialization')),
            ],
        ),
    ]