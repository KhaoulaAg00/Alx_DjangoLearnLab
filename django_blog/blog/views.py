from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DeleteView, DetailView

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    template_name_suffix = 'form'
    success_url = 'accounts/profile'


class Login(LoginView):
    template_name = 'blog/login.html'


@login_required
def ProfileView(request):
    user = request.user

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, "blog/profile.html", {'form': form})


# class Logout(LogoutView):
#     template_name = 'blog/logout.html'
