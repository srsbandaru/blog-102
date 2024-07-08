from django.urls import path
from . import views

app_name = "followers"

urlpatterns = [
    path("<str:user>", views.MyFollowers.as_view(), name = "followers_list")
]