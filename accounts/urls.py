from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('', register, name='register')
]