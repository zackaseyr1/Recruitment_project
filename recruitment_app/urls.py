from django.urls import path
from .views import JobApplicationView, thank_you_view

urlpatterns = [
    path('', JobApplicationView.as_view(), name='job_application'),
    path('thank_you/', thank_you_view, name='thank_you'),
]
