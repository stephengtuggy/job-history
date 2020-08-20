from django.urls import path
from .views import IndexView, JobTimePeriodDetailView

app_name = 'jobHistory'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', JobTimePeriodDetailView.as_view(), name='job-time-period-detail'),
]
