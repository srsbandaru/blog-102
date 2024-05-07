from django.shortcuts import render, redirect 
from .models import Profile
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
import os


# Create your views here.
class UserProfile(DetailView):
    template_name = "profiles/profile_detail.html"
    model = Profile
    http_method_names = ["get"]
    context_object_name = "profile"
    pk_url_kwarg = 'pk'

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