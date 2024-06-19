from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm
from django.contrib import messages

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
class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')
    model = Post
    context_object_name = "form"
    http_method_names = ["get", "post"]
    fields = ["title", "content", "image"]

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            context = {
                'form':form
            }
            return render(request, self.template_name, context)
        
        obj = form.save(commit = False)
        obj.owner = self.request.user
        obj.save()
        

        messages.success(request, "Your post has been created successfully.")
        return redirect(self.success_url)

# Post Update
class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = "blog/post_form.html"
    # success_url = reverse_lazy('blog:post_list')
    model = Post
    pk_url_kwarg = 'pk'
    context_object_name = "form"
    http_method_names = ['get', 'post']
    # fields = ["title", "content"]
    form_class = PostForm
    # success_message = "Your post has been updated successfully."

    # Update Post with Image
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if post.owner == self.request.user:
            if request.FILES:
                post.image.delete()
            form = PostForm(request.POST, request.FILES, instance=post)
            if not form.is_valid():
                context = {
                    'form':form
                }
                return render(request, self.template_name, context)
            
            form.save()
            messages.success(request, "Your post has been updated successfully.")
        else:
            messages.error(request, "You are not an author of the post.")
        
        return redirect(self.get_success_url())

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
class PostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'blog/post_confirm_delete.html'
    model = Post 
    context_object_name = "post"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy("blog:post_list")
    http_method_names = ['get', 'post']
    # success_message = "Your post has been deleted successfully."

    def get_queryset(self):
        queryset = self.model.objects.filter(id = self.kwargs["pk"])
        return queryset
    
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(self.model, id=self.kwargs['pk'])
        if post.owner == self.request.user:
            post.image.delete()
            post.delete()
            messages.success(request, "Your post has been deleted successfully.")
        else:
            messages.error(request, "You are not an author of the post.")
        return redirect(self.success_url)
    
class MyPostList(LoginRequiredMixin, ListView):
    model = Post
    http_method_names = ['get']
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(owner=self.request.user)
        return queryset