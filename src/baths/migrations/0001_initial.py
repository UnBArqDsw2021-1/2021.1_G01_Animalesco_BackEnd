# Generated by Django 3.2.7 on 2021-09-25 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bath_date', models.DateField(verbose_name='Bath date')),
                ('next_bath_date', models.DateField(blank=True, null=True, verbose_name='Next bath date')),
                ('location_bath', models.DateField(blank=True, null=True, verbose_name='Location bath')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baths', to='animals.pet')),
            ],
            options={
                'unique_together': {('bath_date', 'next_bath_date', 'pet')},
            },
        ),
    ]
