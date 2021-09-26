from products.models import Products
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView,
    DestroyAPIView
)

from .serializers import (
    CreateProductsSerializers,
    ListProductsSerializers,
    UpdateProductsSerializers,
    DeleteProductsSerializer
)

class CreateProductsView(CreateAPIView):
    """Create products"""
    serializer_class = CreateProductsSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListProductsView(ListAPIView):
    serializer_class = ListProductsSerializers
    
    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset

class UpdateProductsView(UpdateAPIView):
    serializer_class = UpdateProductsSerializers
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset

class DeleteProductsView(DestroyAPIView):
    serializer_class = DeleteProductsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Products.objects.all()    
        return queryset
