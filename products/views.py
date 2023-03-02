from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import ProductCategory, Maker

from .serializers import (
    ProductCategorySerializer,
    MakerSerializer,
)

class ProductCategoryListView(ListAPIView):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()

class MakerListView(ListAPIView):
    serializer_class = MakerSerializer
    queryset = Maker.objects.all()