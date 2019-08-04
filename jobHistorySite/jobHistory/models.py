from django.db import models
from django.utils.translation import gettext_lazy as _


class Employer(models.Model):
    class Meta:
        verbose_name = _('Employer')
    
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
    can_contact                         = models.BooleanField(null=False, verbose_name=_('Can Contact?'))

    def __str__(self):
        return self.title + " @ " + str(self.employer)


class JobTimePeriod(models.Model):
    class Meta:
        verbose_name = _('Job Time Period')
    
    position                            = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name=_('Position'))
    start_year                          = models.PositiveIntegerField(null=False, verbose_name=_('Start Year'))
    start_month                         = models.PositiveSmallIntegerField(null=True, verbose_name=_('Start Month'))
    start_day                           = models.PositiveSmallIntegerField(null=True, verbose_name=_('Start Day'))
    is_current_position                 = models.BooleanField(null=False, default=True, verbose_name=_('Current Position?'))
    end_year                            = models.PositiveIntegerField(null=True, verbose_name=_('End Year'))
    end_month                           = models.PositiveSmallIntegerField(null=True, verbose_name=_('End Month'))
    end_day                             = models.PositiveSmallIntegerField(null=True, verbose_name=_('End Day'))
    starting_pay                        = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Starting Pay'))
    ending_pay                          = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Ending Pay'))
    hours_per_week                      = models.PositiveSmallIntegerField(null=True, verbose_name=_('Hours per Week'))
    contributions_and_accomplishments   = models.TextField(blank=True, null=False, verbose_name=_('Contributions and Accomplishments'))
    work_city                           = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work City'))
    work_county_or_parish               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work County or Parish'))
    work_state_or_province              = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work State or Province'))
    work_zip_or_postal_code             = models.CharField(max_length=50, blank=True, null=False, verbose_name=_('Work Zip Code or Postal Code'))
    work_country                        = models.CharField(max_length=200, blank=True, null=False, verbose_name=_('Work Country'))

    def __str__(self):
        retVal = self.position.__str__()
        retVal += " from "
        retVal += self.start_year.__str__()
        if self.start_month is not None:
            retVal += "-" + self.start_month.__str__()
            if self.start_day is not None:
                retVal += "-" + self.start_day.__str__()
        retVal += " to "
        if self.is_current_position:
            retVal += "present"
        else:
            retVal += self.end_year.__str__()
            if self.end_month is not None:
                retVal += "-" + self.end_month.__str__()
                if self.end_day is not None:
                    retVal += "-" + self.end_day.__str__()
        return retVal
