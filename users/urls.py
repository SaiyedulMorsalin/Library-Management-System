from django.urls import path
from .views import UserProfileView, UserLoginView

urlpatterns = [
    # "users/profile/logout",
    path("user/profile/", UserProfileView.as_view(), name="user_profile"),
    path("login/", UserLoginView.as_view(), name="user_login"),
    # path("user/logout/", UserLogout, name="user_logout"),
    # path("register", RegisterView, name="user_register"),
    # path("user/profile/edit", UserEditProfile, name="user_edit_profile"),
    # path("user/account/deposit/", user_deposit, name="user_account_deposit"),
    # path("user/borrowing/history/", borrow_history, name="user_borrow_history"),
]
