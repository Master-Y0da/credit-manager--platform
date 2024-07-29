
from django.core.management.base import BaseCommand
from rest_framework_api_key.models import APIKey

class Command(BaseCommand):
    help = 'Create a global API key'

    def handle(self, *args, **kwargs):
        api_key, key = APIKey.objects.create_key(name="admin-global-key")
        self.stdout.write(self.style.SUCCESS(f"Global admin API key: {key}"))
