from jobportal import views
from django.urls import path
from django.views.generic import TemplateView

app_name = "jobportal"

urlpatterns = [
    
    # urls for function based views  //  pages
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),

    # Authentication
    # path("login/", views.login, name="login"),
    # path("register/", views.register, name="register"),
    path("ForgotPassword/", views.ForgotPassword, name="ForgotPassword"),
    path("editProfile/", views.editProfile, name="editProfile"),
    
    # Communication
    path("announcement/", views.announcement, name="announcement"),
    
    # urls for class based views
    path("homeview/", views.HomeView.as_view(), name="homeview"),
    path("aboutview/", views.AboutView.as_view(), name="aboutview"),
    path("contactview/", views.ContactView.as_view(), name="contactview"),
    path("registerview/", views.RegisterView.as_view(), name="registerview"),
    path("loginview/", views.LoginView.as_view(), name="loginview"),
    path("ForgotPasswordView/",views.ForgotPasswordView.as_view(),name="ForgotPasswordView/",),
    
    # company Dashboard
    path("CompanyDashboard/", views.CompanyDashboard.as_view(), name="CompanyDashboard"),
    path("CompanyProfiles/", views.CompanyProfiles.as_view(), name="CompanyProfiles"),
    path("CompanyActivityTracking/", views.CompanyActivityTracking.as_view(), name="CompanyActivityTracking"),
    path("CompanySuspension/",views.CompanySuspension.as_view(),name="CompanySuspension"),
    path("CompanyFeedback/", views.CompanyFeedback.as_view(), name="CompanyFeedback"),
    
    # User Dashboard
    path("UserDashboard/", views.UserDashboard.as_view(), name="UserDashboard"),
    path("UserProfiles/", views.UserProfiles.as_view(), name="UserProfiles"),
    path("UserActivityTracking/",views.UserActivityTracking.as_view(),name="UserActivityTracking"),
    path("UserSuspension/", views.UserSuspension.as_view(), name="UserSuspension"),
    path("UserFeedback/", views.UserFeedback.as_view(), name="UserFeedback"),
    
    # Job Management
    path("JobListingDashboard/",views.JobListingDashboard.as_view(),name="JobListingDashboard"),
    path("JobPostingEditing/",views.JobPostingEditing.as_view(),name="JobPostingEditing"),
    path("JobCategoryManagement/",views.JobCategoryManagement.as_view(),name="JobCategoryManagement"),
    path("JobApplicationTracking/",views.JobApplicationTracking.as_view(),name="JobApplicationTracking"),
    path("JobStatusManagement/",views.JobStatusManagement.as_view(),name="JobStatusManagement",),
    
    # ReportsAndAnalytics
    path("ReportsAndAnalytics/", views.ReportsAndAnalytics, name="ReportsAndAnalytics"),
    path("ViewReportsAndAnalytics/",views.ViewReportsAndAnalytics,name="ViewReportsAndAnalytics",),
    
    # Settings and Configuration
    path("PaymentSettings/", views.PaymentSettings, name="PaymentSettings"),
    
    
]
