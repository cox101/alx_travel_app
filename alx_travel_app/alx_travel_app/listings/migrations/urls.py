from django.urls import path
from .views import ListingListCreateView, ListingRetrieveUpdateDestroyView

urlpatterns = [
    path('', ListingListCreateView.as_view(), name='listing-list-create'),
    path('<int:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),
]