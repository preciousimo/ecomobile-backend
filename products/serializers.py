from rest_framework import serializers

from products.models import ProductCategory, Maker, Product

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        depth = 1