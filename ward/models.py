from django.db import models
from django.utils import timezone
from content.models import Category
from autoslug import AutoSlugField
from user.models import MyUser

class Ward(models.Model):
   
    name = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,  
        related_name='wards'       
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        limit_choices_to={'name__in': ['Events & Notice']},
        null=True 
    )
    
    title = models.CharField(max_length=100,null=True,blank=True)
    body = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='ward/', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Ward for {self.name.username}' 
