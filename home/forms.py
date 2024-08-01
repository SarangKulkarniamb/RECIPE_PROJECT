from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Recipe
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','email','password1','password2']
        
class RecipeForm(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ("title","description","difficulty","procedure","category","ingredients","recp_img")

        