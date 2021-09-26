from django.urls import path

from .views import (
    CreateUserView,
    ListUserView, 
    UpdateUserView, 
)

app_name = "accounts"

urlpatterns = [
    path("create-user", CreateUserView.as_view(), name="create-user"),
    path("list-user", ListUserView.as_view(), name="list-user"),
    path("update-user/<int:pk>", UpdateUserView.as_view(), name="list-user"),
]
