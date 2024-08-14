from django.urls import path
from . import views

urlpatterns = [
    path("book/<int:book_id>/", views.borrow_now, name="borrow_now"),
    path(
        "book/confirmation/<int:order_id>/",
        views.borrow_confirmation,
        name="borrow_conf",
    ),
]
