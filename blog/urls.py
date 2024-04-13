from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name = "post_list"),
    path("details/<int:pk>", views.PostDetail.as_view(), name = "post_detail"),
    path("create", views.PostCreate.as_view(), name = "post_create"),
    path("update/<int:pk>", views.PostUpdate.as_view(), name = "post_update")
]