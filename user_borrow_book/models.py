from django.db import models
from books.models import Book
from django.contrib.auth.models import User

# Create your models here.


class BorrowBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    borrow_at = models.DateTimeField(auto_now_add=True)
