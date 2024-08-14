from django.shortcuts import render
from django.views.generic import TemplateView
from categories.models import Category
from books.models import Book

# Create your views here.


# class HomePage(TemplateView):
#     template_name = "index.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category_slug = self.kwargs.get("category_slug")
#         if category_slug:
#             category = Category.objects.get(slug=category_slug)
#             context["books"] = Book.objects.filter(category=category)
#         else:
#             context["books"] = Book.objects.all()

#         context["categories"] = Category.objects.all()
#         return context


def HomePage(request, category_slug=None):
    books = Book.objects.all()[:12]
    if category_slug:
        category = Category.objects.get(slug=category_slug)
        books = Book.objects.filter(categories=category)
    categories = Category.objects.all()
    book_price_list = []
    for book in books:
        book_price = book.borrow_price - book.discount_price
        book_price_list.append(book_price)

    print(book_price_list)
    return render(
        request,
        "index.html",
        {"books": books, "categories": categories, "book_price_list": book_price_list},
    )
