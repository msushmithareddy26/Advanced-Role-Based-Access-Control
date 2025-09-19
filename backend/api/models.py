# backend/api/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

ROLE_CHOICES = [
    ("admin","Admin"),
    ("recruiter","Recruiter"),
    ("hiring_manager","Hiring Manager"),
]

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role="recruiter", **extra):
        if not email:
            raise ValueError("Users must have email")
        email = self.normalize_email(email)
        user = self.model(email=email, role=role, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password, **extra):
        user = self.create_user(email, password, role="admin", **extra)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="recruiter")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="candidates")
    assigned_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # hiring manager
    resume = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
