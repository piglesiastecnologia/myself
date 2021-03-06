# Generated by Django 4.0.3 on 2022-04-05 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('Other', 'Other')], max_length=30)),
                ('other_gender', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=30)),
                ('summary', models.TextField()),
                ('job_position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socialmedia', models.CharField(choices=[('FB', 'Facebook'), ('IG', 'Instagram'), ('LINKEDIN', 'Linkedin'), ('Other', 'Other')], max_length=30)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('type', models.IntegerField(choices=[(1, 'Listening'), (2, 'Reading'), (3, 'Speaking'), (4, 'Writing')])),
                ('proficiency', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('street_number', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informations.person')),
            ],
        ),
    ]
