from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .models import Book
from .forms import AddBookForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView

# Create your views here.


class BookDetail(DetailView):
    model = Book
    template_name = "book_detail.html"
    pk_url_kwarg = "id"
    context_object_name = "book"


class ShowAllBook(ListView):
    model = Book
    template_name = "all_books.html"

    context_object_name = "all_books"


class AddBook(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("home_page")

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)
