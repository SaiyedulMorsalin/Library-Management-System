from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm
from django.contrib import messages


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "transaction_form.html"
    success_url = reverse_lazy("home_page")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs


class DepositMoney(TransactionCreateMixin):

    form_class = DepositForm

    def form_valid(self, form):
        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        if amount is None or account is None:
            messages.error(self.request, "Invalid deposit operation.")
            return self.form_invalid(form)

        try:
            account.balance += amount
            print("Deposit Success")
            account.save(update_fields=["balance"])
            messages.success(
                self.request,
                f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully',
            )
            # send_transaction_email(
            #     self.request.user,
            #     amount,
            #     "transaction_email.html",
            #     self.title,
            # )
            return super().form_valid(form)
        except Exception as e:
            messages.error(
                self.request, "An error occurred while processing your deposit."
            )
            print(e)

            return self.form_invalid(form)
