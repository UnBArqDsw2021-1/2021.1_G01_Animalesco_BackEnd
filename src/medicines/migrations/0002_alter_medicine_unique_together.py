# Generated by Django 3.2.7 on 2021-09-17 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='medicine',
            unique_together=set(),
        ),
    ]
