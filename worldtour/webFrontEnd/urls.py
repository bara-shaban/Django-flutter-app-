from django.urls import path
from . import views

app_name = "webFrontEnd"

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/", views.blog, name="blog"),  # This is important
    path("about/", views.about, name="about"),
    path("post1/", views.post1, name="post1"),
    path("post2/", views.post2, name="post2"),
    # Add other paths here
]
