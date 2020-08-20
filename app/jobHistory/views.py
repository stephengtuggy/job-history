import operator

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView #, SingleObjectTemplateResponseMixin

from .models import JobTimePeriod


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'jobHistory/index.html'
    context_object_name = 'chronological_job_list'

    def get_queryset(self):
        job_time_periods = JobTimePeriod.objects.all()
        return sorted(job_time_periods, key=operator.attrgetter('endDate'), reverse=True)


class JobTimePeriodDetailView(LoginRequiredMixin, DetailView):
    model = JobTimePeriod


