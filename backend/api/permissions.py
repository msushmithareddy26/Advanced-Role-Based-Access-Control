# backend/api/permissions.py
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "admin")

class IsRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "recruiter")

class IsHiringManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "hiring_manager")

# Example combined permission for Job endpoints:
class JobPermission(permissions.BasePermission):
    """
    Admin: full CRUD
    Recruiter: create, read, update but not delete
    Hiring Manager: read only
    """
    def has_permission(self, request, view):
        role = getattr(request.user, "role", None)
        if not role: return False
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        if role == "admin":
            return True
        if role == "recruiter":
            # allow POST and PUT/PATCH but not DELETE
            return request.method in ("POST","PUT","PATCH")
        return False  # hiring manager cannot modify
