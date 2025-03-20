from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view


class ProductCategoryList(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


class ProviderList(ListAPIView):
    serializer_class = ProviderSerializer
    queryset = Provider.objects.all()


class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
