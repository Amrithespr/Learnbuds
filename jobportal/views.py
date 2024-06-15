from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib import auth
from .models import Jobportal,CompanyDashboard,CompanyProfiles,CompanyActivityTracking,CompanySuspension,CompanyFeedback
from .models import Jobportal,UserDashboard,UserProfiles,UserActivityTracking,UserSuspension,UserFeedback
from .models import JobApplicationTracking,JobCategoryManagement,JobListingDashboard,JobPostingEditing,JobStatusManagement


# Create your views here.



# class based views

class HomeView(ListView):

    model = Jobportal
    template_name = 'base.html'
    context_object_name = 'job'
    

class AboutView(ListView):

    model = Jobportal
    template_name = 'about.html'
    context_object_name = 'job'
    
    
class ContactView(ListView):

    model = Jobportal
    template_name = 'contact.html'
    context_object_name = 'job'
    

class RegisterView(ListView):

    model = Jobportal
    template_name = 'register.html'
    context_object_name = 'job'
    
    
class LoginView(ListView):

    model = Jobportal
    template_name = 'login.html'
    context_object_name = 'job'   
     

class ForgotPasswordView(ListView):

    model = Jobportal
    template_name = 'ForgotPassword.html'
    context_object_name = 'job'
    
    
# Company Dashboard

class CompanyDashboard(ListView):

    model = CompanyDashboard
    # template_name = 'CompanyDashboard/CompanyDashboard.html'
    template_name = 'accordion.html'
    context_object_name = 'CompanyDashboard'


class CompanyProfiles(ListView):

    model = CompanyProfiles
    template_name = 'CompanyDashboard/profiles.html'
    context_object_name = 'CompanyProfiles'


class CompanyActivityTracking(ListView):

    model = CompanyActivityTracking
    template_name = 'CompanyDashboard/activity.html'
    context_object_name = 'CompanyActivityTracking'
    
    
class CompanySuspension(ListView):

    model = CompanySuspension
    template_name = 'CompanyDashboard/suspension.html'
    context_object_name = 'CompanySuspension'
    
    
class CompanyFeedback(ListView):

    model = CompanyFeedback
    template_name = 'CompanyDashboard/feedback.html'
    context_object_name = 'CompanyFeedback'


# User Dashboard

class UserDashboard(ListView):

    model = UserDashboard
    template_name = 'UserDashboard/index.html'
    context_object_name = 'UserDashboard'


class UserProfiles(ListView):

    model = UserProfiles
    template_name = 'UserDashboard/profiles.html'
    context_object_name = 'UserProfiles'


class UserActivityTracking(ListView):

    model = UserActivityTracking
    template_name = 'UserDashboard/activity.html'
    context_object_name = 'UserActivityTracking'
    
    
class UserSuspension(ListView):

    model = UserSuspension
    template_name = 'UserDashboard/suspension.html'
    context_object_name = 'UserSuspension'
    
    
class UserFeedback(ListView):

    model = UserFeedback
    template_name = 'UserDashboard/feedback.html'
    context_object_name = 'UserFeedback'


# Job Management

class JobApplicationTracking(ListView):

    model = JobApplicationTracking
    template_name = 'JobManagement/JobApplicationTracking.html'
    context_object_name = 'JobApplicationTracking'


class JobCategoryManagement(ListView):

    model = JobCategoryManagement
    template_name = 'JobManagement/JobCategoryManagement.html'
    context_object_name = 'JobCategoryManagement'


class JobListingDashboard(ListView):

    model = JobListingDashboard
    template_name = 'JobManagement/JobListingDashboard.html'
    context_object_name = 'JobListingDashboard'


class JobPostingEditing(ListView):

    model = JobPostingEditing
    template_name = 'JobManagement/JobPostingEditing.html'
    context_object_name = 'JobPostingEditing'


class JobStatusManagement(ListView):

    model = JobStatusManagement
    template_name = 'JobManagement/JobStatusManagement.html'
    context_object_name = 'JobStatusManagement'




# Function based views


def home(request):
    return render (request, 'MainDashboard.html')


def about(request):
    return render (request, 'about.html')


def contact(request):
    return render (request, 'contact.html')


def register(request):
    return render (request, 'register.html')


def login(request):
    return render (request, 'login.html')


def ForgotPassword(request):
    return render (request, 'ForgotPassword.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')


# ReportsAndAnalytics

def ReportsAndAnalytics(request):
    return render (request, 'ReportsAndAnalytics/ReportsAndAnalytics.html')


def ViewReportsAndAnalytics(request):
    return render (request, 'ReportsAndAnalytics/ViewReportsAndAnalytics.html')


# Settings and Configuration

def PaymentSettings(request):
    return render (request, 'PaymentSettings/PaymentSettings.html')