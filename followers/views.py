from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from followers.models import Follower

# Create your views here.
class MyFollowers(LoginRequiredMixin, ListView):
    model = Follower
    context_object_name = "myFollowers"

    def get_queryset(self):
        current_logged_in_user = self.request.user
        queryset = self.model.objects.filter(following=current_logged_in_user)
        return queryset