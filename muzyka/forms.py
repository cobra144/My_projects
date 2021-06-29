from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']





class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    photo_user = forms.ImageField(label='Photo', required=False)
    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2','photo_user')



class LoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput)#hides password on input


class QuestionForm(ModelForm):
    class Meta:
        model = Galeria
        fields = ['nazwa','category','rok_powstania','zdjecie','opis']
        widgets = {
            'question': Textarea(attrs={'cols': 40, 'rows': 20}),
        }

class dodaj_do_kolekcji(ModelForm):
    class Meta:
        model = UlubionyAlbum
        fields = ['user','albumy']
