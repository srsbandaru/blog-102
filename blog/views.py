from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.messages.views import SuccessMessageMixin

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
class PostCreate(SuccessMessageMixin, CreateView):
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')
    model = Post
    context_object_name = "form"
    http_method_names = ["get", "post"]
    fields = ["title", "content"]
    success_message = "Your post has been created successfully."

# Post Update
class PostUpdate(SuccessMessageMixin, UpdateView):
    template_name = "blog/post_form.html"
    # success_url = reverse_lazy('blog:post_list')
    model = Post
    pk_url_kwarg = 'pk'
    context_object_name = "form"
    http_method_names = ['get', 'post',]
    fields = ["title", "content"]
    success_message = "Your post has been updated successfully."

    # Customise the queryset
    def get_queryset(self):
        queryset = self.model.objects.filter(id = self.kwargs["pk"])
        return queryset
    
    # Customise the success_url
    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs = {"pk":self.kwargs["pk"]})
    
    # Add your context data
    def get_context_data(self, **kwargs):
        # Get context data
        context = super(PostUpdate, self).get_context_data(**kwargs)
        # Add your context data
        context["form_type"] = "Update"
        return context

# Post Delete
class PostDelete(SuccessMessageMixin, DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    model = Post 
    context_object_name = "post"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("blog:post_list")
    http_method_names = ['get', 'post']
    success_message = "Your post has been deleted succeesfully."

    def get_queryset(self):
        queryset = self.model.objects.filter(id = self.kwargs["pk"])
        return queryset
