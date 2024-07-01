from django.shortcuts import render, redirect 
from .models import Profile
from django.views.generic import DetailView, UpdateView, View
from django.urls import reverse_lazy
import os
from django.contrib.auth.models import User
from blog.models import Post 
from followers.models import Follower
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest, JsonResponse


# Create your views here.
class UserProfile(DetailView):
    template_name = "profiles/profile_detail.html"
    model = Profile
    http_method_names = ["get"]
    context_object_name = "profile"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        user = self.get_object()
        owner_id = User.objects.filter(username=user)[0].id
        context = super().get_context_data(**kwargs)
        context['total_posts'] = Post.objects.filter(owner=owner_id).count()
        context['total_followers'] = Follower.objects.filter(following=owner_id).count()

        if self.request.user.is_authenticated:
            context['you_follow'] = Follower.objects.filter(following=owner_id, followed_by=self.request.user).exists()
        return context 

class UpdateProfile(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'mobile', 'address']
    
    def get_success_url(self):
        return reverse_lazy("profiles:profile_detail", kwargs = {"pk":self.kwargs["pk"]})
    
def UpdateProfilePicture(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if profile.image:
                os.remove(profile.image.path)
            profile.image = request.FILES['image_document']
        profile.save()
        success_url = '/profile/detail/' + str(profile.id)
        return redirect(success_url)
    context = {
        'profile':profile
        }
    return render(request, 'profiles/picture_form.html', context)

def DeleteProfilePicture(request, pk):
    profile = Profile.objects.get(id=pk)
    os.remove(profile.image.path)
    profile.image=""
    profile.save()
    success_url = '/profile/detail/' + str(profile.id)
    return redirect(success_url)

class FollowView(LoginRequiredMixin, View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "id" not in data:
            return HttpResponseBadRequest("Missing action or id")
        
        try:
            other_user = User.objects.get(id=data["id"])
        except:
            return HttpResponseBadRequest("User not found")
        
        if data['action'] == "follow":
            follower, created = Follower.objects.get_or_create(followed_by=request.user, following=other_user)
        else:
            try:
                follower, created = Follower.objects.get_or_create(followed_by=request.user, following=other_user)
            except:
                follower = None 

            if follower:
                follower.delete()

        json_data = {
            'success' : True,
            'wording' : 'Unfollow' if data['action'] == 'follow' else 'Follow',
        }

        return JsonResponse(json_data)