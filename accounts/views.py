from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
from .forms import DepositForm


# Create your views here.
class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "transaction_form.html"
    success_url = reverse_lazy("user_profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs


class DepositMoney(TransactionCreateMixin):
    form_class = DepositForm

    def form_valid(self, form):

        user_account = getattr(self.request.user, "account", None)
        if user_account is None:
            return redirect("user_login")

        amount = form.cleaned_data.get("amount")
        account = self.request.user.account
        print(user_account)
        if amount is None or account is None:
            messages.error(self.request, "Invalid deposit operation.")
            return self.form_invalid(form)
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
            messages.error(
                self.request, "An error occurred while processing your deposit."
            )
            print(e)
            return self.form_invalid(form)
