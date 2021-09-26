from cart.models import Carts
from products.models import Products
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateCartsSerializer, ConcluirCartsSerializer, ListCartsSerializer

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView,
    DestroyAPIView
)

class CreateCartsView(CreateAPIView):
    serializer_class = CreateCartsSerializer

class ListCartsView(ListAPIView):
    serializer_class = ListCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset

class DeleteCartsView(DestroyAPIView):
    serializer_class = ConcluirCartsSerializer

    def get_queryset(self):
        queryset = Carts.objects.all()    
        return queryset
