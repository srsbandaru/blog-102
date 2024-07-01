from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("detail/<int:pk>", views.UserProfile.as_view(), name = 'profile_detail'),
    path("update/<int:pk>", views.UpdateProfile.as_view(), name = 'profile_update'),
    path("update/picture/<int:pk>", views.UpdateProfilePicture, name = 'picture_update'),
    path("delete/picture/<int:pk>", views.DeleteProfilePicture, name = 'picture_delete'),
    path("detail/<int:pk>/follow/", views.FollowView.as_view(), name = 'follow')
]