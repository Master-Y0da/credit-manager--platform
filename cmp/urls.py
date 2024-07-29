from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cmp.permissions import Permisos

schema_view = get_schema_view(
    openapi.Info(
        title="Credit Manager Platform API",
        default_version='v1',
        description="Test backend"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('cmp.apps.customer.urls')),
    path('api/v1/', include('cmp.apps.loan.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]