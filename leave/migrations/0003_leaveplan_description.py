# Generated by Django 3.0.7 on 2020-08-06 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_leaveplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveplan',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
