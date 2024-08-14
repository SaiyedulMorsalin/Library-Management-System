from django.contrib import admin
from .models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "stk_quantity", "borrow_price", "is_available")
