# seeds/seed_data.py
from django.core.management.base import BaseCommand
from api.models import User  # Replace 'myapp' and 'Person' with your actual app and model

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        # Seed data creation
        data = [
            {'password': 'demo','email': 'john@example.com'},
            {'password': 'Demo','email': 'demo@example'},
            # Add more data as needed
        ]

        # Populate the database with the seed data
        for item in data:
            User.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))