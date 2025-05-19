from django.db import models
from django.core.validators import MinValueValidator

class Listing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('HOUSE', 'House'),
        ('APARTMENT', 'Apartment'),
        ('VILLA', 'Villa'),
        ('HOTEL', 'Hotel'),
        ('RESORT', 'Resort'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES,
        default='APARTMENT'
    )
    num_bedrooms = models.PositiveIntegerField()
    num_bathrooms = models.PositiveIntegerField()
    max_guests = models.PositiveIntegerField()
    amenities = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.city}, {self.country}"

    class Meta:
        ordering = ['-created_at']