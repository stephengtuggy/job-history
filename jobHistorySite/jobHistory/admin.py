from django.contrib import admin

from .models import Employer, Position, JobTimePeriod


class JobTimePeriodInline(admin.TabularInline):
    model = JobTimePeriod


class PositionAdmin(admin.ModelAdmin):
    inlines = [JobTimePeriodInline]


admin.site.register(Employer)
admin.site.register(Position, PositionAdmin)
