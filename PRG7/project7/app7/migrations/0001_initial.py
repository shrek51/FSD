# Generated by Django 5.0.6 on 2024-07-21 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=10, unique=True)),
                ('student_name', models.CharField(max_length=80)),
                ('student_sem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=200)),
                ('Languages_used', models.CharField(max_length=200)),
                ('Duration_in_days', models.IntegerField()),
                ('Selected_student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app7.student')),
            ],
        ),
    ]
