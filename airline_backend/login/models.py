from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, default='user')  # Add default

    def __str__(self):
        return f"{self.user.username} - {self.title}"
