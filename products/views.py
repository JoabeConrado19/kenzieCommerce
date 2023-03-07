from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Product
from .serializer import ProductSerializer

# Create your views here.

class ProductView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        id = self.request.query_params.get('id')
        if category:
            queryset = queryset.filter(category=category)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if id:
            queryset = queryset.filter(id=id)
        return queryset

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


 