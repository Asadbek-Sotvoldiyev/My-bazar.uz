from users.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from .forms import LoginForm, RegisterForm, ProfileForm

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    form = LoginForm()
    data = {
        'form':form,
    }

    return render(request,'users/login.html',context=data)

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = User()
                user.username = form.cleaned_data.get('username')
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = form.cleaned_data.get('email')
                user.set_password(form.cleaned_data.get('password'))
                user.save()
                return HttpResponseRedirect(reverse('users:login'))
            except:
                return HttpResponseRedirect(reverse('index'))


    else:
        form = RegisterForm()

    data = {
        'form':form,
    }
    return render(request,'users/register.html', context=data)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class ProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('index')

    def get_object(self):
        return self.request.user
