from django.shortcuts import render
from .forms import *

# Create your views here.



# Create your views here.
def register(request):
    context = {
        'form': UserCreationForm()
    }
    return render(request, 'accounts/register.html', context)