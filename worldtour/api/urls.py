from django.urls import path
from .view import views, auth


urlpatterns = [
    path("", views.getData, name="getData"),
    path("<int:id>/", views.getData, name="getData"),
    path("add/", views.addData, name="addData"),
    path("register/", auth.register_user, name="register"),
    # path('getAllUsers/', auth.get_all_users, name='getData'),
    path("deleteUser/<int:id>/", auth.delete_user, name="deleteUser"),
]
