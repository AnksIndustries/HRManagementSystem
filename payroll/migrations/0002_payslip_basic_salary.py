# Generated by Django 3.0.7 on 2020-07-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='basic_salary',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
