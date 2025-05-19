from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'address',
            'city',
            'country',
            'price_per_night',
            'property_type',
            'num_bedrooms',
            'num_bathrooms',
            'max_guests',
            'amenities',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']