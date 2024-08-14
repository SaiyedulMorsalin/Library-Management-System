from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from .models import Book
from .forms import AddBookForm
from django.urls import reverse_lazy

# Create your views here.


class BookDetail(TemplateView):
    template_name = "book_detail.html"


class ShowAllBook(ListView):
    model = Book
    template_name = "all_books.html"
    context_object_name = "all_books"


class AddBook(FormView):
    form_class = AddBookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):

        form.save()
        return super().form_valid(form)
