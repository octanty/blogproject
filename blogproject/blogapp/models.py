from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators




class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    #cover_photo = models.ImageField(upload_to='covers/', null=True, blank=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
        )

    def __str__(self):
        return self.username


    

class Blog(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='blogs')
    title = models.CharField(max_length=100, null=True, blank=True)
    #cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)


# This is the string representation of the object
    def __str__(self):
        return self.title

    