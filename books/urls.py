from django.urls import path
from .views import BookDetail

urlpatterns = [path("details/", BookDetail.as_view(), name="book_detail")]
