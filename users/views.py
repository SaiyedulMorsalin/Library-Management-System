from django.shortcuts import render
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, UpdateView, FormView, ListView
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

from user_borrow_book.models import BorrowBook


# Create your views here.
class UserRegisterView(FormView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy("user_register")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "You Are Successfully Registered!!")
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "login.html"
    form_class = UserLoginForm

    def get_success_url(self):
        messages.success(self.request, "You Are Successfully Login!!")
        return reverse_lazy("home_page")


class UserLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, "You have been successfully logged out!")
        return reverse_lazy("home_page")


class UserProfileView(ListView):
    model = BorrowBook
    template_name = "user_profile.html"
    context_object_name = "all_borrow"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user_account"] = "Some value"


class EditUserProfile(UpdateView):

    pass
