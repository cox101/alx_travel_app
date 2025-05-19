from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country', 'price_per_night', 'property_type', 'is_active')
    list_filter = ('is_active', 'property_type', 'city', 'country')
    search_fields = ('title', 'description', 'address', 'city', 'country')
    ordering = ('-created_at',)
