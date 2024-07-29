from rest_framework.permissions import BasePermission
from django.conf import settings

class Permisos(BasePermission):
    def has_permission(self, request, view):
        swagger_paths = [
            '/swagger/',  
            '/swagger.json',
            '/swagger.yaml',
            '/swagger/?format=openapi',
            '/redoc/',
        ]

        if any(request.path.startswith(path) for path in swagger_paths):
            return True

        api_key = request.headers.get('Authorization')
        if api_key == f"Api-Key {settings.API_KEY}":
            return True

        return False
