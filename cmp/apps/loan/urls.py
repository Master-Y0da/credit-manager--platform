from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewset

router = DefaultRouter()
router.register(r'loans', LoanViewset)

urlpatterns = [
    path('', include(router.urls)),
]
