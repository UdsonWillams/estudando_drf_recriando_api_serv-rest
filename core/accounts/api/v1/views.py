from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView, 
    UpdateAPIView)

from .serializers import (
    CreateUserSerializer, 
    ListUserSerializer, 
    UpdateUserSerializer,
)

from accounts.models import User

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    
class ListUserView(ListAPIView):
    queryset = User.objects.all() 
    serializer_class = ListUserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class UpdateUserView(UpdateAPIView):
    serializer_class = UpdateUserSerializer
    queryset = User.objects.all() 
