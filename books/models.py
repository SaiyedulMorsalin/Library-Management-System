from django.db import models
from authors.models import Author
from categories.models import Category

# Create your models here.


class Book(models.Model):
    book_image = models.ImageField(upload_to="media/book_images")
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=Category)
    book_content = models.TextField()
    description = models.TextField()
    isbn_number = models.CharField(max_length=13, unique=True)
    borrow_price = models.PositiveIntegerField()
    stk_quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=50)

    def now_price(self):
        return self.borrow_price - self.discount_price
