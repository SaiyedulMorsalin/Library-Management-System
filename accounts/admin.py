from django.contrib import admin
from .models import UserAccount


# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("user__username", "account_create_date", "balance")
