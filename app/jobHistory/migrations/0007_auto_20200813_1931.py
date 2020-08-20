# Generated by Django 2.2.15 on 2020-08-13 19:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobHistory', '0006_auto_20200808_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='end_day',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='End Day'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='end_month',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='End Month'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='start_day',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='Start Day'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='start_month',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)], verbose_name='Start Month'),
        ),
    ]
