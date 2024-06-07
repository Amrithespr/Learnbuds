from django.shortcuts import render
from django.views.generic import ListView
from .models import Jobportal


# Create your views here.



# class based views

class HomeView(ListView):

    model = Jobportal
    template_name = 'home.html'
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
    template_name = 'forgot_password.html'
    context_object_name = 'job'
    
    

# Function based views


def home(request):
    return render (request, 'home.html')


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