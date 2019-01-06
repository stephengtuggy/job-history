from django.db import models
from django.utils.translation import gettext_lazy as _


class Employer(models.Model):
    short_name                          = models.CharField(max_length=50, unique=True, blank=False, null=False)
    long_name                           = models.CharField(max_length=254, unique=True, blank=False, null=True)
    industry                            = models.CharField(max_length=254, blank=True, null=False)
    phone                               = models.CharField(max_length=50, blank=True, null=False)
    email                               = models.EmailField(blank=True, null=False)
    addr1                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 1"))
    addr2                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 2"))
    addr3                               = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Address Line 3"))
    city                                = models.CharField(max_length=200, blank=True, null=False)
    county_or_parish                    = models.CharField(max_length=200, blank=True, null=False)
    state_or_province                   = models.CharField(max_length=200, blank=True, null=False)
    zip_or_postal_code                  = models.CharField(max_length=50, blank=True, null=False)
    country                             = models.CharField(max_length=200, blank=True, null=False)

    def __str__(self):
        return self.short_name


class Position(models.Model):
    employer                            = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title                               = models.CharField(max_length=200, blank=False, null=False)
    responsibilities                    = models.TextField(blank=True, null=False)
    contributions_and_accomplishments   = models.TextField(blank=True, null=False)
    supervisor_name_prefix              = models.CharField(max_length=50, blank=True, null=False)
    supervisor_given_name               = models.CharField(max_length=200, blank=False, null=False)
    supervisor_middle_name              = models.CharField(max_length=200, blank=True, null=False)
    supervisor_surname                  = models.CharField(max_length=200, blank=False, null=False)
    supervisor_name_suffix              = models.CharField(max_length=50, blank=True, null=False)
    supervisor_phone                    = models.CharField(max_length=50, blank=True, null=False)
    supervisor_email                    = models.EmailField(blank=True, null=False)
    supervisor_addr1                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 1"))
    supervisor_addr2                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 2"))
    supervisor_addr3                    = models.CharField(max_length=200, blank=True, null=False, verbose_name=_("Supervisor Address Line 3"))
    supervisor_city                     = models.CharField(max_length=200, blank=True, null=False)
    supervisor_county_or_parish         = models.CharField(max_length=200, blank=True, null=False)
    supervisor_state_or_province        = models.CharField(max_length=200, blank=True, null=False)
    supervisor_zip_or_postal_code       = models.CharField(max_length=50, blank=True, null=False)
    supervisor_country                  = models.CharField(max_length=200, blank=True, null=False)
    can_contact                         = models.BooleanField(null=False)

    def __str__(self):
        return self.title + " @ " + self.employer.__str__()


class JobTimePeriod(models.Model):
    position                            = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_year                          = models.PositiveIntegerField(null=False)
    start_month                         = models.PositiveSmallIntegerField(null=True)
    start_day                           = models.PositiveSmallIntegerField(null=True)
    is_current_position                 = models.BooleanField(null=False, default=True)
    end_year                            = models.PositiveIntegerField(null=True)
    end_month                           = models.PositiveSmallIntegerField(null=True)
    end_day                             = models.PositiveSmallIntegerField(null=True)
    starting_pay                        = models.CharField(max_length=50, blank=False, null=False)
    ending_pay                          = models.CharField(max_length=50, blank=False, null=False)
    hours_per_week                      = models.PositiveSmallIntegerField(null=True)
    contributions_and_accomplishments   = models.TextField(blank=True, null=False)    
    work_city                           = models.CharField(max_length=200, blank=True, null=False)
    work_county_or_parish               = models.CharField(max_length=200, blank=True, null=False)
    work_state_or_province              = models.CharField(max_length=200, blank=True, null=False)
    work_zip_or_postal_code             = models.CharField(max_length=50, blank=True, null=False)
    work_country                        = models.CharField(max_length=200, blank=True, null=False)

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
