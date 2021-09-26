# Generated by Django 3.2.7 on 2021-09-26 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VetVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vet_clinic', models.CharField(max_length=100, verbose_name='Veterinary clinic name')),
                ('description', models.TextField(blank=True, max_length=350, null=True, verbose_name='Description of the visit purpose')),
                ('visit_date', models.DateField(verbose_name='Vet visit date')),
                ('next_visit_date', models.DateField(blank=True, null=True, verbose_name='Next vet visit date')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vet_visits', to='animals.pet')),
            ],
        ),
    ]
