from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
class UserLoginView(LoginView):

    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.user
        login(self.request, user)
        return super().form_valid(form)


class UserLogoutView:
    pass


class UserProfileView:
    pass


class UserEditProfile:
    pass
