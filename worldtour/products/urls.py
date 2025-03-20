from django.urls import path
from .views import *

app_name = "products"

urlpatterns = [
    path("categories/", ProductCategoryList.as_view(), name="categories"),
    path("providers/", ProviderList.as_view(), name="providers"),
    path("", ProductList.as_view(), name="products"),
]
