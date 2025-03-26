from django.urls import path
from .views import CustomUserRegister, CustomUserDelete

app_name = "users"

urlpatterns = [
    path("register/", CustomUserRegister.as_view(), name="register"),
    path("delete/", CustomUserDelete.as_view(), name="delete"),
]
