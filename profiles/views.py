from django.shortcuts import render
from .models import Profile
from django.views.generic import DetailView

# Create your views here.
class UserProfile(DetailView):
    template_name = "profiles/profile_details.html"
    model = Profile
    http_method_names = ["get"]
    context_object_name = "profile"
    pk_url_kwarg = 'pk'
