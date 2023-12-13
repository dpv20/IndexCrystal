from django.db import models
from django.conf import settings
import os

def get_profile_pic_filename(instance, filename):
    ext = filename.split('.')[-1]  # Extracts file extension
    username_part = instance.email.split('@')[0]  # Extracts the part before '@'
    new_filename = f"{username_part}.{ext}"  # Constructs the new filename
    return os.path.join('profile_pics', new_filename)  # Saves in 'profile_pics' directory


class ExternalWebpageUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    webpage_url = models.URLField()
    external_username = models.CharField(max_length=100)
    external_password = models.CharField(max_length=100)

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to=get_profile_pic_filename, blank=True, null=True)

