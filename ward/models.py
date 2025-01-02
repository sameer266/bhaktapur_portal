from django.db import models
from django.utils import timezone
from content.models import Category
from autoslug import AutoSlugField
from user.models import MyUser

class Ward(models.Model):
    # Keep the field name as 'name', but it is a ForeignKey to the MyUser model
    name = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,  # CASCADE to delete related Ward when the user is deleted
        related_name='wards'       # Allows reverse relation to get a user's wards (user.wards)
    )
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        limit_choices_to={'name__in': ['Events & Notice']},
        null=True  # Allow category to be blank if needed
    )
    
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True, max_length=50)
    image = models.ImageField(upload_to='ward/', blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Ward for {self.name.username}'  # Use 'name' field here, which links to MyUser
