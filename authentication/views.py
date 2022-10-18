from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm, SignupForm, DeleteProfileForm
from django.views.generic import View
from django.conf import settings
from .models import User


# Connexion en mode class
class LoginPage(View):
    form_cass = LoginForm
    template_name = "authentication/login.html"
    def get(self,request):
        form = self.form_cass()
        message = ''
        return render(request, self.template_name, {'form': form, 'message': message})

    def post(self, request):
            form = self.form_cass(request.POST or None)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password'))
                if user is not None:
                    login(request, user)
                    return redirect(settings.LOGIN_REDIRECT_URL)

            message = f"Identification invalide "
            return render(request,self.template_name, {'form': form, 'message': message})


# Connexion
def Login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                 message = f"Identification invalide "
    return render(request,"authentication/login.html",{'form':form,'message':message})

# Déconnexion
def logout_page(request):
    logout(request)
    return redirect('home')

# Insriptions
def sigup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    context = {'form':form}
    return  render(request,"authentication/signup.html",context)





#Détail d'un profil
def detail_profile(request,id):
    profile = get_object_or_404(User,id=id)
    context = {'profile': profile}
    return  render(request,"authentication/profile_detail.html",context)


# Modifier Profile d'utilisateur
def edit_profile(request,profile_id):
    profile = get_object_or_404(User,id=profile_id)
    edit_profile = SignupForm(instance=profile)
    delete_profile = DeleteProfileForm()
    if request.method == 'POST':
        if "edit_profile" in request.POST:
            edit_profile = SignupForm(request.POST,request.FILES,instance=profile)
            if edit_profile.is_valid():
               edit_profile.save()
               return redirect('home')
    if request.method == 'POST':
        if "delete_profile" in request.POST:
            delete_profile = DeleteProfileForm(request.POST)
            if delete_profile.is_valid():
                profile.delete()
                return redirect("home")
    context = {'edit_profile': edit_profile,
               "delete_profile": delete_profile
               }
    return  render(request,"authentication/edit_profile.html",context)