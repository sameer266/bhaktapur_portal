from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Models
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=100)
    body =RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='culture',default=False)  # Custom upload path based on category
    
    def __str__(self):
        return self.title
