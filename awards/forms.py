from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import Project,Profile


class RegForm(ModelForm):
    class Meta:
        model = User 
        fields = ['username','email','password','first_name', 'last_name']
        widgets = {
            'password':forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','project_pic','link']

class EditProfile(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

