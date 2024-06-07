from django.contrib import admin
from .models import Jobportal,CompanyDashboard,CompanyProfiles,CompanyActivityTracking,CompanySuspension,CompanyFeedback

# Register your models here.


admin.site.register(Jobportal)
admin.site.register(CompanyDashboard)
admin.site.register(CompanyProfiles)
admin.site.register(CompanyActivityTracking)
admin.site.register(CompanySuspension)
admin.site.register(CompanyFeedback)
