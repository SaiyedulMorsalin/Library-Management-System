from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = ""
    success_url = ""
    pass


class DepositMoney(TransactionCreateMixin):
    pass
