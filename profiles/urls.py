from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("detail/<int:pk>", views.UserProfile.as_view(), name = 'profile_detail')
]