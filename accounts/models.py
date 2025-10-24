from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom User model (already set up in your case)
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.role})"


# Course model now has a ForeignKey to the User model
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')  # link courses to users
    duration = models.PositiveIntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.title
