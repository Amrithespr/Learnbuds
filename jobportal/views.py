from django.shortcuts import render
from django.views.generic import ListView
from .models import Jobportal

# Create your views here.


# class based views

class cbv_home(ListView):
    model = Jobportal
    template_name = 'home.html'
    context_object_name = 'job'
    
class cbv_about(ListView):
    model = Jobportal
    template_name = 'about.html'
    context_object_name = 'job'
    
class cbv_contact(ListView):
    model = Jobportal
    template_name = 'contact.html'
    context_object_name = 'job'
    
class cbv_register(ListView):
    model = Jobportal
    template_name = 'register.html'
    context_object_name = 'job'
    
class cbv_login(ListView):
    model = Jobportal
    template_name = 'login.html'
    context_object_name = 'job'   
     
class cbv_forgot_password(ListView):
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

def forgot_password(request):
    return render (request, 'forgot_password.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')