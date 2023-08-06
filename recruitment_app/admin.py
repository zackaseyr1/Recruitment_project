from django.contrib import admin
from .models import JobApplication


class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'country', 'state', 'gender', 'occupation', 'submission_date')
    list_filter = ('gender', 'occupation', 'submission_date')
    search_fields = ('name', 'email', 'phone_number', 'country', 'state', 'occupation')

    def get_actions(self, request):
        actions = super().get_actions(request)
        # Remove the default "delete_selected" action
        del actions['delete_selected']
        return actions

    def download_emails(self, request, queryset):
        # This function generates a CSV file containing only the email addresses
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="emails.csv"'

        writer = csv.writer(response)
        writer.writerow(['Email'])

        for application in queryset:
            writer.writerow([application.email])

        return response

    download_emails.short_description = 'Download emails (CSV)'

    actions = [download_emails]


admin.site.register(JobApplication, JobApplicationAdmin)
