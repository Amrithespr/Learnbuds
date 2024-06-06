from . import views
from django.urls import path


app_name = 'jobportal'


urlpatterns = [
    
    # urls for function based views
    
    path('',                     views.home,                          name='home'),
    path('about/',               views.about,                         name='about'),
    path('contact/',             views.contact,                       name='contact'),
    
    path('register/',            views.register,                      name='register'),
    path('login/',               views.login,                         name='login'),
    path('forgot_password/',     views.forgot_password,               name='forgot_password'),
    
    
    # urls for class based views
    
    path('cbv_home/',            views.cbv_home.as_view(),            name='cbv_home'),
    path('cbv_about/',           views.cbv_about.as_view(),           name='cbv_about'),
    path('cbv_contact/',         views.cbv_contact.as_view(),         name='cbv_contact'),
    
    path('cbv_register/',            views.cbv_register.as_view(),        name='cbv_register'),
    path('cbv_login/',           views.cbv_login.as_view(),           name='cbv_login'),
    path('cbv_forgot_password/', views.cbv_forgot_password.as_view(), name='cbv_forgot_password'),
    
]
