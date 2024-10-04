from django.db import models
from ward.models import Ward
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.


class MyUser(AbstractUser):
    ROLE_CHOICES=[
        ('ward_officer','ward officer'),
    ]
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)
    ward=models.OneToOneField(Ward,on_delete=models.CASCADE,null=True,blank=True )
    
    groups = models.ManyToManyField(Group, related_name='myuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='myuser_permissions', blank=True)


