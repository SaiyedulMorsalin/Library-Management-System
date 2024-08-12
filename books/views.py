from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class BookDetail(TemplateView):
    template_name = "book_detail.html"
