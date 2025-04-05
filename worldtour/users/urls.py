from django.urls import path
from .views import CustomUserRegister, CustomUserDelete, GetCustomUser

app_name = "users"

urlpatterns = [
    path("register/", CustomUserRegister.as_view(), name="register"),
    path("delete/", CustomUserDelete.as_view(), name="delete"),
    path("get/", GetCustomUser.as_view(), name="get_user"),
]
