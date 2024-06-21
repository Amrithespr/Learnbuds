from django.forms import ModelForm, Form
from django.forms import TextInput, PasswordInput, CharField
from django.core.validators import MinLengthValidator
from .models import *


class LoginForm(Form):
    username = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Username',
        widget = TextInput({
            'class': 'form-control'
        })
    )

    password = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Password',
        widget = PasswordInput({
            'class': 'form-control'
        })
    )

class UserCreationForm(ModelForm):

    confirm_password = CharField(
        max_length = 25,
        min_length = 8,
        required = True,
        validators = [
            MinLengthValidator(8, 'The password is too short.')
        ],
        widget = PasswordInput({
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'username': TextInput({
                'class': 'form-control'
            }),
            'first_name': TextInput({
                'class': 'form-control'
            }),
            'last_name': TextInput({
                'class': 'form-control'
            }),
            'password': PasswordInput({
                'class': 'form-control'
            }),
        }
        
    
class UserProfileForm(Form):

    phone = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Phone',
        widget = TextInput({
            'class': 'form-control'
        })
    )   
     
    email = CharField(
        max_length = 15,
        min_length = 2,
        required = True,
        label = 'Email',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    country = CharField(
        max_length = 15,
        min_length = 2,
        required = True,
        label = 'Country',
        widget = TextInput({
            'class': 'form-control'
        })
    )

    street_address = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Street Address',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    city = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'City,Country*',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    postcode = CharField(
        max_length = 15,
        min_length = 4,
        required = True,
        label = 'Postcode',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    cv = CharField(
        
        required = True,
        label = 'Upload CV',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    photo = CharField(
        
        required = True,
        label = ' Photo',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    jobtitle = CharField(
        max_length = 15,
        min_length = 4,
        required = False,
        label = 'Job title',
        widget = TextInput({
            'class': 'form-control'
        })
    )
    
    company = CharField(
    max_length = 15,
    min_length = 4,
    required = False,
    label = 'Company',
    widget = TextInput({
        'class': 'form-control'
    })
    )