# Generated by Django 2.2.15 on 2020-08-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobHistory', '0008_auto_20200820_1614'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='jobtimeperiod',
            constraint=models.UniqueConstraint(fields=('position', 'start_year', 'is_current_position', 'end_year'), name='job_time_period_must_be_unique'),
        ),
    ]
