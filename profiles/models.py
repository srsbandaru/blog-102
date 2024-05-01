from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.dispatch import receiver
from django.db.models.signals import post_save

# User Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.TextField(blank=True)
    mobile = models.CharField(max_length=16, blank=True)
    image = ImageField(upload_to="profiles", blank=True)

    def __str__(self):
        return self.user.username
    
# Signal for creating a user profile when we sign up
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
