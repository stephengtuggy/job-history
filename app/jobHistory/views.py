import operator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from .models import JobTimePeriod

# Create your views here.
class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'jobHistory/index.html'
    context_object_name = 'chronological_job_list'

    def get_queryset(self):
        job_time_periods = JobTimePeriod.objects.all()
        return sorted(job_time_periods, key=operator.attrgetter('endDate'), reverse=True)
