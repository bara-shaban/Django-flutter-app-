from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('<int:id>/', views.getData, name='getData'),
    path('add/', views.addData, name='addData'),
]