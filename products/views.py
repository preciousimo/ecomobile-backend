from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product, ProductCategory, Maker

from .serializers import (
    ProductCategorySerializer,
    MakerSerializer,
    ProductSerializer,
)

class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class MakerListView(ListAPIView):
    serializer_class = MakerSerializer
    queryset = Maker.objects.all()

class ProductsListView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
