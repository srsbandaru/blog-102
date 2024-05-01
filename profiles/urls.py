from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("detail/<int:pk>", views.UserProfile.as_view(), name = 'profile_detail'),
    path("update/<int:pk>", views.UpdateProfile.as_view(), name = 'profile_update')
]