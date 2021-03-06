# Generated by Django 2.2.4 on 2019-08-04 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobHistory', '0002_auto_20190106_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='city',
            field=models.CharField(blank=True, max_length=200, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='country',
            field=models.CharField(blank=True, max_length=200, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='county_or_parish',
            field=models.CharField(blank=True, max_length=200, verbose_name='County or Parish'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='industry',
            field=models.CharField(blank=True, max_length=254, verbose_name='Industry'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='long_name',
            field=models.CharField(max_length=254, null=True, unique=True, verbose_name='Long Name'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='short_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Short Name'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='state_or_province',
            field=models.CharField(blank=True, max_length=200, verbose_name='State or Province'),
        ),
        migrations.AlterField(
            model_name='employer',
            name='zip_or_postal_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Zip Code or Postal Code'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='contributions_and_accomplishments',
            field=models.TextField(blank=True, verbose_name='Contributions and Accomplishments'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='end_day',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='End Day'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='end_month',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='End Month'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='end_year',
            field=models.PositiveIntegerField(null=True, verbose_name='End Year'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='ending_pay',
            field=models.CharField(max_length=50, verbose_name='Ending Pay'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='hours_per_week',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Hours per Week'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='is_current_position',
            field=models.BooleanField(default=True, verbose_name='Current Position?'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobHistory.Position', verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='start_day',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Start Day'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='start_month',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Start Month'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='start_year',
            field=models.PositiveIntegerField(verbose_name='Start Year'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='starting_pay',
            field=models.CharField(max_length=50, verbose_name='Starting Pay'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='work_city',
            field=models.CharField(blank=True, max_length=200, verbose_name='Work City'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='work_country',
            field=models.CharField(blank=True, max_length=200, verbose_name='Work Country'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='work_county_or_parish',
            field=models.CharField(blank=True, max_length=200, verbose_name='Work County or Parish'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='work_state_or_province',
            field=models.CharField(blank=True, max_length=200, verbose_name='Work State or Province'),
        ),
        migrations.AlterField(
            model_name='jobtimeperiod',
            name='work_zip_or_postal_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Work Zip Code or Postal Code'),
        ),
        migrations.AlterField(
            model_name='position',
            name='can_contact',
            field=models.BooleanField(verbose_name='Can Contact?'),
        ),
        migrations.AlterField(
            model_name='position',
            name='contributions_and_accomplishments',
            field=models.TextField(blank=True, verbose_name='Contributions and Accomplishments'),
        ),
        migrations.AlterField(
            model_name='position',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobHistory.Employer', verbose_name='Employer'),
        ),
        migrations.AlterField(
            model_name='position',
            name='responsibilities',
            field=models.TextField(blank=True, verbose_name='Responsibilities'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_city',
            field=models.CharField(blank=True, max_length=200, verbose_name='Supervisor City'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_country',
            field=models.CharField(blank=True, max_length=200, verbose_name='Supervisor Country'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_county_or_parish',
            field=models.CharField(blank=True, max_length=200, verbose_name='Supervisor County or Parish'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Supervisor Email'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_given_name',
            field=models.CharField(max_length=200, verbose_name='Supervisor Given Name'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_middle_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Supervisor Middle Name'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_name_prefix',
            field=models.CharField(blank=True, max_length=50, verbose_name='Supervisor Name Prefix'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_name_suffix',
            field=models.CharField(blank=True, max_length=50, verbose_name='Supervisor Name Suffix'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='Supervisor Phone'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_state_or_province',
            field=models.CharField(blank=True, max_length=200, verbose_name='Supervisor State or Province'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_surname',
            field=models.CharField(max_length=200, verbose_name='Supervisor Surname'),
        ),
        migrations.AlterField(
            model_name='position',
            name='supervisor_zip_or_postal_code',
            field=models.CharField(blank=True, max_length=50, verbose_name='Supervisor Zip Code or Postal Code'),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]
