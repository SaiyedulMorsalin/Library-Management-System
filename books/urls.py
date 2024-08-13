from django.urls import path
from .views import BookDetail

urlpatterns = [
    path("details/", BookDetail.as_view(), name="book_detail"),
    # path("show/all/", ShowAllBooks_view, name="show_all_books"),
    # path("categories/", BookCategories, name="books_category"),
    # path("popular/", books_popular_views, name="popular_books"),
]
