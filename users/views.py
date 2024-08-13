from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, UpdateView, FormView


# Create your views here.
class UserRegisterView(FormView):
    template_name = "register.html"
    form_class = ".forms/register_form"
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("home_page")


class UserLogoutView(LogoutView):
    def get_success_ulr(self):
        if self.request.user.is_authenticated:
            logout(self.request)

        return reverse_lazy("home_page")


class UserProfileView(TemplateView):
    template_name = "user_profile.html"


class EditUserProfile(UpdateView):
    pass
