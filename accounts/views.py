# from django.shortcuts import render,HttpResponse
# from django.contrib.auth import authenticate, login
# from .forms import *

# # Create your views here.



# # Create your views here.
# def user_login(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = LoginForm()
#         return render(request, 'accounts/login.html', context)
#     elif request.method == 'POST':
#         form = LoginForm(data = request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is None:
#                 return HttpResponse("Invalid data")
#             login(request, user)
#             return HttpResponse('User login successful.')
#         # If the form is not valid
#         context['form'] = form
#         return render(request, 'accounts/login.html', context)

# def register(request):
#     context = {}
#     if request.method == 'GET':
#         context['form'] = UserCreationForm()
#         return render(request, 'accounts/register.html', context)
#     else:
#         form = UserCreationForm(data = request.POST)
#         if not form.is_valid():
#             context['form'] = form
#             return render(request, 'accounts/register.html', context)
#         user = form.save(commit=False)
#         user.set_password(user.password)
#         user.save()
#         return HttpResponse('User registered successfully.')
#     return render(request, 'accounts/register.html', context)

# def profile(request):
#     context = {
#         'form': UserProfileForm()
#     }
#     return render(request, 'accounts/profile.html', context)



from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView
from django.urls import reverse, reverse_lazy
from .forms import *
from .models import User, Address


# Create your views here.
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # Ensure you import your LoginForm from the correct location

class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Invalid username or password')
        return render(request, self.template_name, {'form': form})


class RegisterView(View):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        user = form.save(commit=False)
        user.password = form.cleaned_data['password']
        user.save()
        return redirect('accounts:login')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')


class AddressListVew(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'accounts/address_list.html'
    context_object_name = 'data'

    def get_queryset(self):
        queryset = super(AddressListVew, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class AddressCreateView(LoginRequiredMixin, CreateView):
    form_class = AddressCreateForm
    template_name = 'accounts/address_create.html'
    success_url = reverse_lazy('accounts:address_list')