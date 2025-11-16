from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['listing_id', 'title', 'description', 'host', 'price_per_night', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer(read_only=True)
    class Meta:
        model = Booking
        fields = ['booking_id', 'listing', 'user', 'check_in', 'check_out', 'status', 'created_at']
