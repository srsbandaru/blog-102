from django.forms import ModelForm
from django.forms import ImageField, FileInput

from blog.models import Post

class PostForm(ModelForm):
    image = ImageField(widget=FileInput, label="Upload New Image")
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']