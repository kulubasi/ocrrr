
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class uploadform(forms.ModelForm):
    class Meta:
        model=myimages
        fields= ['img']

class uploadpdfform(forms.ModelForm):
    class Meta:
        model=mypdfs
        fields= ['pdf']


# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=101)
#     last_name = forms.CharField(max_length=101)
#     email = forms.EmailField()
#     password2=None

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

# class BookForm(forms.ModelForm):
#     class Meta:
#         model=Book
#         #fields=('title','author','pdf','cover')
#         fields=['title','author','pdf','cover']


# class uploadform(forms.Form):
#     #first_name= forms.CharField(max_length=100)
#     imge= forms.ImageField(max_length=100)
