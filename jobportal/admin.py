from django.contrib import admin
from .models import Jobportal,CompanyDashboard,CompanyProfiles,CompanyActivityTracking,CompanySuspension,CompanyFeedback
from .models import Jobportal,UserDashboard,UserProfiles,UserActivityTracking,UserSuspension,UserFeedback
from .models import JobApplicationTracking,JobCategoryManagement,JobListingDashboard,JobPostingEditing,JobStatusManagement

# Register your models here.


admin.site.register(Jobportal)

# Company Dashboard

admin.site.register(CompanyDashboard)
admin.site.register(CompanyProfiles)
admin.site.register(CompanyActivityTracking)
admin.site.register(CompanySuspension)
admin.site.register(CompanyFeedback)

# User Dashboard

admin.site.register(UserDashboard)
admin.site.register(UserProfiles)
admin.site.register(UserActivityTracking)
admin.site.register(UserSuspension)
admin.site.register(UserFeedback)

# Job Management

admin.site.register(JobApplicationTracking)
admin.site.register(JobCategoryManagement)
admin.site.register(JobListingDashboard)
admin.site.register(JobPostingEditing)
admin.site.register(JobStatusManagement)
