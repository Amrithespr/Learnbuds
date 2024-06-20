from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login
from .forms import *

# Create your views here.



# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'accounts/login.html', context)
    elif request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                return HttpResponse("Invalid data")
            login(request, user)
            return HttpResponse('User login successful.')
        # If the form is not valid
        context['form'] = form
        return render(request, 'accounts/login.html', context)

def register(request):
    context = {
        'form': UserCreationForm()
    }
    return render(request, 'accounts/register.html', context)