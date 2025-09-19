# backend/api/management/commands/create_sample_users.py
from django.core.management.base import BaseCommand
from api.models import User

class Command(BaseCommand):
    help = "Create sample users"

    def handle(self, *args, **kwargs):
        users = [
            ("admin@example.com","adminpass","admin"),
            ("rec1@example.com","recpass","recruiter"),
            ("hm1@example.com","hmpass","hiring_manager")
        ]
        for email, password, role in users:
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(email=email, password=password, role=role)
                self.stdout.write(self.style.SUCCESS(f"Created {email}"))
            else:
                self.stdout.write(f"{email} exists")
