from django import forms
from .models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["amount", "account"]

    def __init__(self, *args, **kwargs):

        self.account = kwargs.pop("account", None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):

        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save(commit=commit)
