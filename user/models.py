from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class MyUser(AbstractUser):
    ROLE_CHOICES = [
        ('ward_officer', 'ward officer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    
    # Ward can be assigned to multiple users, so remove the uniqueness constraint
    ward = models.IntegerField(null=True, blank=True,unique=True)  # Removed unique=True

    # Group and Permission management is already provided by AbstractUser
    # If you need custom management, you can leave them as is
    groups = models.ManyToManyField(Group, related_name='myuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='myuser_permissions', blank=True)
