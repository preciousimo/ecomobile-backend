from django.urls import path
from .views import ProductCategoryListView, MakerListView

app_name = "products"

urlpatterns = [
    path("categories", ProductCategoryListView.as_view(), name="categories-list"),
    path("makers", MakerListView.as_view(), name="makers-list"),
]