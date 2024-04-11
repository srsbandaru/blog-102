from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post

# Create your views here.

# Post List
class PostList(ListView):
    template_name = "blog/post_list.html"
    model = Post
    queryset = Post.objects.all()
    context_object_name = "post_list"
    http_method_names = ["get"]
