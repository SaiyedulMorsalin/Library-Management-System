# from django.urls import path
# from . import views

# urlpatterns = [
#     path("book/<int:id>/", views.borrow_now, name="borrow_now"),
#     path(
#         "borrow/<int:borrow_id>/confirmation/",
#         views.borrow_confirmation,
#         name="borrow_conf",
#     ),
# ]
from django.urls import path
from .views import borrow_now, borrow_confirmation

urlpatterns = [
    path("borrow_now/<int:book_id>/", borrow_now, name="borrow_now"),
    path("borrow_conf/<int:order_id>/", borrow_confirmation, name="borrow_conf"),
]
