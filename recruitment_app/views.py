from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import JobApplicationForm

class JobApplicationView(FormView):
    template_name = 'recruitment_app/job_application_form.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def thank_you_view(request):
    template_name = 'recruitment_app/thank_you.html'
    return render(request, template_name)
