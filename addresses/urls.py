from django.urls import path
from .views import AddressView


urlpatterns = [
    path("address/", AddressView.as_view()),
    path("address/<int:pk>/", AddressView.as_view()),
]
