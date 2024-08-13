from django.urls import path
from .views import UserProfileView, UserLoginView

urlpatterns = [
    # "users/profile/logout",
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("user/login/", UserLoginView.as_view(), name="user_login"),
]
