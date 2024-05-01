from django.shortcuts import render
from .models import Profile
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class UserProfile(DetailView):
    template_name = "profiles/profile_details.html"
    model = Profile
    http_method_names = ["get"]
    context_object_name = "profile"
    pk_url_kwarg = 'pk'

class UpdateProfile(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'mobile', 'address']
    
    def get_success_url(self):
        return reverse_lazy("profiles:profile_detail", kwargs = {"pk":self.kwargs["pk"]})