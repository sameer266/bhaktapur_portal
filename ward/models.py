from django.db import models
from django.utils import timezone
from content.models import Category
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField

class Ward(models.Model):
    name = models.CharField(max_length=10)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        limit_choices_to={'name__in': ['Events & Notice']},
        default=None
    )
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    slug = AutoSlugField(populate_from='title',unique=True,max_length=50)
    image = models.ImageField(upload_to='ward/', blank=True,null=True)
    date_created = models.DateTimeField(default=timezone.now)


    def clean(self):
        super().clean()
        if len(self.name) > 5:
            raise ValidationError("Name should be less than or equal to 5 characters")

    def __str__(self) -> str:
        return self.name
