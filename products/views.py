from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory

from .serializers import (
    ProductCategorySerializer
)

class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()