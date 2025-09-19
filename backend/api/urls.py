# backend/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import JobViewSet, CandidateViewSet, MyTokenObtainPairView

# Set up DRF router for viewsets
router = DefaultRouter()
router.register(r"jobs", JobViewSet, basename="job")
router.register(r"candidates", CandidateViewSet, basename="candidate")

# Define URL patterns
urlpatterns = [
    path("login/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),  # Custom JWT login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),   # Refresh token
    path("", include(router.urls)),                                             # Jobs & Candidates endpoints
]
