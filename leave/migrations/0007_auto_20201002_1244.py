# Generated by Django 3.0.7 on 2020-10-02 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_statutorydeduction'),
        ('leave', '0006_auto_20201002_1241'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='leaverecord',
            unique_together={('employee', 'leave_year')},
        ),
    ]
