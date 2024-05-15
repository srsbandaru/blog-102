from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to='posts', blank=True)

    def __str__(self):
        return self.title[0:25]
    