import random
import uuid
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed database with sample listings'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding database...')

        hosts = User.objects.filter(is_staff=False)[:5]  # Take first 5 users
        if not hosts:
            self.stdout.write(self.style.WARNING("No users found to assign as hosts."))
            return

        for i in range(10):  # create 10 sample listings
            listing = Listing.objects.create(
                listing_id=uuid.uuid4(),
                title=f"Sample Listing {i+1}",
                description=f"This is the description for listing {i+1}.",
                host=random.choice(hosts),
                price_per_night=random.randint(50, 500)
            )
            self.stdout.write(self.style.SUCCESS(f"Created listing {listing.title}"))

        self.stdout.write(self.style.SUCCESS('Database seeding completed!'))
