from django.db import models
from django.contrib.auth.models import User
class UserInfo (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profilepic=models.ImageField(blank=True,upload_to='profilepics')
    portfoliosite=models.URLField(blank=True)

    def __str__(self):
        return self.user.username

# Create your models here.
