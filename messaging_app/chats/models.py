from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.

class User(AbstractUser):

    ROLE_CHOICES = [
    ('guest', 'Guest'),
    ('host', 'Host'),
    ('admin', 'Admin')
]
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(unique=True, null=False)
    password_hash = models.CharField(max_length=50, null=False)
    phone_number = models.PositiveIntegerField(null=True)
    role =models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.first_name + self.last_name} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_host(self):
        return self.role == 'host'

    @property
    def is_guest(self):
        return self.role == 'guest'    
    
class Message(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    message = models.TextField(max_length=2000, null=False)
    sent_at = models.DateTimeField(auto_now_add=True, default=timezone.now)

    def __str__(self):
        return self.message


class Conversation(models.Model):
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participants')
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)


