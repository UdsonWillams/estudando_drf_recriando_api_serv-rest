from django.urls import path

from .views import (
    CreateProductsView,
    ListProductsView,
    UpdateProductsView,
    DeleteProductsView
)

app_name = "accounts"

urlpatterns = [
    path("create-product", CreateProductsView.as_view(), name="create-product"),
    path("list-product", ListProductsView.as_view(), name="list-product"),
    path("update-product/<int:pk>", UpdateProductsView.as_view(), name="update-product"),
    path("delete-product/<int:pk>", DeleteProductsView.as_view(), name="delete-product"),
]
