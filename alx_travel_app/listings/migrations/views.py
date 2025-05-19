from rest_framework import generics, permissions
from .models import Listing
from .serializers import ListingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(is_active=True)
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()