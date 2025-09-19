from rest_framework import viewsets, status
from .models import Job, Candidate, User
from .serializers import JobSerializer, CandidateSerializer, UserSerializer, MyTokenObtainPairSerializer
from .permissions import JobPermission
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated


# login view (uses custom token serializer)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all().order_by("-created_at")
    serializer_class = JobSerializer
    permission_classes = [JobPermission]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# ✅ CandidateViewSet with get_queryset properly defined
class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_queryset(self):
        # Prevent Swagger from crashing during schema generation
        if getattr(self, 'swagger_fake_view', False):
            return Candidate.objects.none()

        user = self.request.user

        if user.is_authenticated:
            if user.role == "hiring_manager":
                return Candidate.objects.filter(job__created_by=user)
            elif user.role == "admin":
                return Candidate.objects.all()

        return Candidate.objects.none()
