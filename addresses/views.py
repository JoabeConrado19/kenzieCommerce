from .models import Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AddressSerializer
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmOrAccountOwner


class AddressView(ListCreateAPIView, UpdateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrAccountOwner]

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
