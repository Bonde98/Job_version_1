from  django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model




class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={"class":'form-control',"placeholder":"Nom d'utilisateur"}))

    password = forms.CharField(label="Mot de passe",
                               widget=forms.PasswordInput(
                                   attrs={"class": 'form-control', "placeholder": "*********"}))


# Class Inscription
class SignupForm(forms.ModelForm):
    WORKER = 'WORKER'
    SUBSCRIBER = 'SUBSCRIBER'
    ROLE_CHOICES = (
        (WORKER, 'Trvailleur'),
        (SUBSCRIBER, 'Abonné')
    )
    HOMME = 'HOMME'
    FEMME = 'FEMME'
    SEXE_CHOICES = (
        (HOMME, 'Homme'),
        (FEMME, 'Femme')
    )

    username = forms.CharField(label="Nom d'utilisateur",
                           widget=forms.TextInput
                           (attrs={"class": "form-control py-3", "placeholder": "Nom d'utilisateur"}))
    profile_photo = forms.ImageField(label='Photo de profile',
                                     widget=forms.FileInput(attrs={'class':'form-control'}))

    email = forms.CharField(label="Adresse Email",
                            widget=forms.EmailInput
                            (attrs={"class": "form-control", "placeholder": "Adresse email"}))
    role = forms.ChoiceField(widget=forms.Select,
                                          choices=ROLE_CHOICES)
    sexe = forms.ChoiceField(widget=forms.Select,
                                     choices=SEXE_CHOICES)
    home_adress = forms.CharField(label="Adresse à Domicile",
                               widget=forms.TextInput
                               (attrs={"class": "form-control", "placeholder": "Adresse à Domicile"}))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput
                                (attrs={"class": "form-control", "placeholder": "**********"}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput
                                (attrs={"class": "form-control", "placeholder": "**********"}))
    # Modification d'un profile
    edit_profile = forms.BooleanField(widget=forms.HiddenInput,initial=True)

    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2','profile_photo','role','sexe','home_adress']

# Supprimer un Profle
class DeleteProfileForm(forms.Form):
    # Supprimer Profile
    delete_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True)
