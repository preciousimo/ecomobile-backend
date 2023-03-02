from django.urls import path
from .views import ProductCategoryListView

app_name = "products"

urlpatterns = [
    path("categories", ProductCategoryListView.as_view(), name="categories-list"),
]