# from django.forms import ModelForm, Form
# from django.forms import TextInput, PasswordInput, CharField
# from django.core.validators import MinLengthValidator
# from .models import *


# class LoginForm(Form):
#     username = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'Username',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )

#     password = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'Password',
#         widget = PasswordInput({
#             'class': 'form-control'
#         })
#     )

# class UserCreationForm(ModelForm):

#     confirm_password = CharField(
#         max_length = 25,
#         min_length = 8,
#         required = True,
#         validators = [
#             MinLengthValidator(8, 'The password is too short.')
#         ],
#         widget = PasswordInput({
#             'class': 'form-control'
#         })
#     )

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'password', 'email']
#         widgets = {
#             'username': TextInput({
#                 'class': 'form-control'
#             }),
#             'first_name': TextInput({
#                 'class': 'form-control'
#             }),
#             'last_name': TextInput({
#                 'class': 'form-control'
#             }),
#             'email': TextInput ({
#                 'class': 'form-control'
#             }),
#             'password': PasswordInput({
#                 'class': 'form-control'
#             }),
#         }
        
    
# class UserProfileForm(Form):

#     phone = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'Phone',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )   
     
#     # email = CharField(
#     #     max_length = 15,
#     #     min_length = 2,
#     #     required = True,
#     #     label = 'Email',
#     #     widget = TextInput({
#     #         'class': 'form-control'
#     #     })
#     # )
#     country = CharField(
#         max_length = 15,
#         min_length = 2,
#         required = True,
#         label = 'Country',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )

#     street_address = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'Street Address',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     city = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'City,Country*',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     postcode = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = True,
#         label = 'Postcode',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     cv = CharField(
        
#         required = True,
#         label = 'Upload CV',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     photo = CharField(
        
#         required = True,
#         label = ' Photo',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     jobtitle = CharField(
#         max_length = 15,
#         min_length = 4,
#         required = False,
#         label = 'Job title',
#         widget = TextInput({
#             'class': 'form-control'
#         })
#     )
    
#     company = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Company',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     education = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Level of Education',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     fieldOfStudy = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Field of study',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     school = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'School',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     skills = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add a Skill',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     certification = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add a Certification or Licences',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     futureJobTitle = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add Job Titles',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     futureJobTypes = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add job types',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     workSchedule = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add work Schedule',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )
    
#     futureSalary = CharField(
#     max_length = 15,
#     min_length = 4,
#     required = False,
#     label = 'Add Salary',
#     widget = TextInput({
#         'class': 'form-control'
#     })
#     )


from django.forms import EmailInput, ModelForm, Form, Select, RadioSelect, CheckboxInput
from django.forms import TextInput, PasswordInput, CharField, Textarea, FileInput
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
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone',
            'profile_photo',
            'dob',
            'short_bio',
            'job_title',
            'gender',
            'country',
            'open_to_hiring'
        ]

        widgets = {
            'username': TextInput({
                'class': 'form-control'
            }),

            'email': EmailInput({
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

            'phone': TextInput({
                'class': 'form-control'
            }),

            'dob': TextInput({
                'class': 'form-control'
            }),

            'short_bio': Textarea({
                'class': 'form-control',
                'rows': '3'
            }),

            'job_title': TextInput({
                'class': 'form-control',
            }),

            'gender': Select({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),

            'open_to_hiring': CheckboxInput(),

            'profile_photo': FileInput({
                'class': 'form-control'
            })
        }


class AddressCreateForm(ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        widgets = {
            'name': TextInput({
                'class': 'form-control'
            }),

            'address_line_1': TextInput({
                'class': 'form-control'
            }),

            'address_line_2': TextInput({
                'class': 'form-control'
            }),

            'address_line_3': TextInput({
                'class': 'form-control'
            }),

            'city': TextInput({
                'class': 'form-control'
            }),

            'state': TextInput({
                'class': 'form-control'
            }),

            'pincode': TextInput({
                'class': 'form-control'
            }),

            'country': Select({
                'class': 'form-control'
            }),

            'phone': TextInput({
                'class': 'form-control'
            }),

            'is_default': CheckboxInput(),
        }