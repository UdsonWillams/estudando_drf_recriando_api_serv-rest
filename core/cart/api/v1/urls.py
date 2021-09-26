from django.urls import path

from .views import (
    CreateCartsView,
    ListCartsView,
    # UpdateProductsView,
    DeleteCartsView
)

app_name = "accounts"

urlpatterns = [
    path("create-cart", CreateCartsView.as_view(), name="create-cart"),
    path("list-cart", ListCartsView.as_view(), name="list-cart"),
    # path("update-product/<int:pk>", UpdateProductsView.as_view(), name="update-user"),
    path("delete-cart/<int:pk>", DeleteCartsView.as_view(), name="delete-user"),
]
