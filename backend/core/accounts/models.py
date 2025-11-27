from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    ROLE_ADMIN = "admin"
    ROLE_EMPLOYER = "employer"
    ROLE_FREELANCER = "freelancer"

    ROLE_CHOICES = [
        (ROLE_ADMIN, "Admin"),
        (ROLE_EMPLOYER, "Employer"),
        (ROLE_FREELANCER, "Freelancer"),
    ]

    role=models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_FREELANCER)
    email_verification = models.BooleanField(default=False)