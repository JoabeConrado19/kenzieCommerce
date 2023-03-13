from django.urls import path
from .views import OrderView, OrderDetailView, DeliveredProductsView


urlpatterns = [
    path("order/", OrderView.as_view()),
    path("order/<int:pk>/", OrderDetailView.as_view()),
    path("order/soldout/", DeliveredProductsView.as_view()),
]
