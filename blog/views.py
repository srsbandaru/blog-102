from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from blog.models import Post

# Create your views here.

# Post List
class PostList(ListView):
    template_name = "blog/post_list.html"
    model = Post
    queryset = Post.objects.all()
    context_object_name = "post_list"
    http_method_names = ["get"]

# Post Detail
class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    model = Post
    context_object_name = "post"
    http_method_names = ["get"]
    pk_url_kwarg = 'pk'

    def get_object(self):
        queryset = get_object_or_404(self.model, id=self.kwargs['pk'])
        return queryset
    
# Post Create
class PostCreate(CreateView):
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')
    model = Post
    context_object_name = "form"
    http_method_names = ["get", "post"]
    fields = ["title", "content"]
