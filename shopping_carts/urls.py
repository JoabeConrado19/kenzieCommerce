from django.urls import path
from .views import ShoppingCartsView


urlpatterns = [
    path("shopping/", ShoppingCartsView.as_view()),
    path("shopping/<int:pk>/", ShoppingCartsView.as_view()),
]