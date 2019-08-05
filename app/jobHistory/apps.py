from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class JobHistoryConfig(AppConfig):
    name = 'jobHistory'
    verbose_name = _("Job History")
