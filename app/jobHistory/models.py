import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Employer(models.Model):
    class Meta:
        verbose_name = _('Employer')
        constraints = [
                        models.UniqueConstraint(fields=['short_name', ], name='employer_must_be_unique'),
                      ]

    short_name                          = models.CharField(max_length=50, unique=True, blank=False, null=False, verbose_name=_('Short Name'))
    long_name                           = models.CharField(max_length=254, unique=True, blank=False, null=True, verbose_name=_('Long Name'))
    industry                            = models.CharField(max_length=254, blank=True, null=False, verbose_name=_('Industry'))
    phone                               = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Phone'))
    email                               = models.EmailField(blank=True, null=False, verbose_name=_('Email'))
    addr1                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 1"))
    addr2                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 2"))
    addr3                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 3"))
    city                                = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('City'))
    county_or_parish                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('County or Parish'))
    state_or_province                   = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('State or Province'))
    zip_or_postal_code                  = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Zip Code or Postal Code'))
    country                             = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Country'))

    def __str__(self):
        return self.short_name


class Position(models.Model):
    class Meta:
        verbose_name = _('Position')
        constraints = [
                        models.UniqueConstraint(fields=['employer', 'title', ], name='position_must_be_unique'),
                      ]

    employer                            = models.ForeignKey(Employer, on_delete=models.CASCADE, verbose_name=_('Employer'))
    title                               = models.CharField(max_length=200, blank=False, null=False, verbose_name=_('Title'))
    responsibilities                    = models.TextField(blank=True, null=False, verbose_name=_('Responsibilities'))
    contributions_and_accomplishments   = models.TextField(blank=True, null=False, verbose_name=_('Contributions and Accomplishments'))
    supervisor_name_prefix              = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Supervisor Name Prefix'))
    supervisor_given_name               = models.CharField(max_length=200, blank=False, null=False, verbose_name=_('Supervisor Given Name'))
    supervisor_middle_name              = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Supervisor Middle Name'))
    supervisor_surname                  = models.CharField(max_length=200, blank=False, null=False, verbose_name=_('Supervisor Surname'))
    supervisor_name_suffix              = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Supervisor Name Suffix'))
    supervisor_phone                    = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Supervisor Phone'))
    supervisor_email                    = models.EmailField(blank=True, null=False, verbose_name=_('Supervisor Email'))
    supervisor_addr1                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 1"))
    supervisor_addr2                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 2"))
    supervisor_addr3                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 3"))
    supervisor_city                     = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Supervisor City'))
    supervisor_county_or_parish         = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Supervisor County or Parish'))
    supervisor_state_or_province        = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Supervisor State or Province'))
    supervisor_zip_or_postal_code       = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Supervisor Zip Code or Postal Code'))
    supervisor_country                  = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Supervisor Country'))
    can_contact                         = models.BooleanField(blank=False, null=False, verbose_name=_('Can Contact?'))

    def __str__(self):
        return self.title + " @ " + str(self.employer)


class JobTimePeriod(models.Model):
    class Meta:
        verbose_name = _('Job Time Period')
        constraints  = [
                        models.CheckConstraint(check=(models.Q(is_current_position__exact=True) | models.Q(end_year__isnull=False)), name='require_end_date_if_not_current_position'),
                        models.CheckConstraint(check=(models.Q(is_current_position__exact=False) | (models.Q(end_year__isnull=True) & models.Q(end_month__isnull=True) & models.Q(end_day__isnull=True))), name='leave_end_date_blank_if_current_position'),
                        models.CheckConstraint(check=(models.Q(start_month__isnull=False) | models.Q(start_day__isnull=True)), name='require_start_month_if_start_day_specified'),
                        models.CheckConstraint(check=(models.Q(end_year__isnull=False) | (models.Q(end_month__isnull=True) & models.Q(end_day__isnull=True))), name='require_end_year_if_end_month_specified'),
                        models.CheckConstraint(check=(models.Q(end_month__isnull=False) | models.Q(end_day__isnull=True)), name='require_end_month_if_end_day_specified')
                       ]

    position                            = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name=_('Position'))
    start_year                          = models.PositiveIntegerField(blank=False, null=False, verbose_name=_('Start Year'))
    start_month                         = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)], verbose_name=_('Start Month'))
    start_day                           = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)], verbose_name=_('Start Day'))
    is_current_position                 = models.BooleanField(blank=False, null=False, default=True, verbose_name=_('Current Position?'))
    end_year                            = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('End Year'))
    end_month                           = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(12)], verbose_name=_('End Month'))
    end_day                             = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(31)], verbose_name=_('End Day'))
    starting_pay                        = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Starting Pay'))
    ending_pay                          = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Ending Pay'))
    hours_per_week                      = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name=_('Hours per Week'))
    contributions_and_accomplishments   = models.TextField(blank=True, null=False, verbose_name=_('Contributions and Accomplishments'))
    work_city                           = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work City'))
    work_county_or_parish               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work County or Parish'))
    work_state_or_province              = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work State or Province'))
    work_zip_or_postal_code             = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Work Zip Code or Postal Code'))
    work_country                        = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work Country'))

    @property
    def startDate(self):
        return datetime.date(self.start_year, self.start_month or 1, self.start_day or 1)

    @property
    def endDate(self):
        if self.is_current_position:
            return datetime.date.today()
        else:
            return datetime.date(self.end_year or datetime.MINYEAR, self.end_month or 1, self.end_day or 1)

    def __str__(self):
        ret_val = str(self.position)
        ret_val += " from "
        try:
            ret_val += str(self.startDate)
        except ValueError as e:
            ret_val += '<Invalid start date value>'
        ret_val += " to "
        if self.is_current_position:
            ret_val += "present"
        else:
            try:
                ret_val += str(self.endDate)
            except ValueError as e:
                ret_val += '<Invalid end date value>'
        return ret_val

    def clean(self):
        if self.is_current_position and self.end_year is not None:
            raise ValidationError(_('Leave end date blank if this is your current position'))
        elif self.end_year is None and not self.is_current_position:
            raise ValidationError(_('End date (at least end year) is required if this is not your current position'))
        elif self.start_month is None and self.start_day is not None:
            raise ValidationError(_('Start month is required if start day is specified'))
        elif self.end_year is None and (self.end_month is not None or self.end_day is not None):
            raise ValidationError(_('End year is required if end month or end day is specified'))
        elif self.end_month is None and self.end_day is not None:
            raise ValidationError(_('End month is required if end day is specified'))
