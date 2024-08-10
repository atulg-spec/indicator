from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.contrib.auth.models import AbstractUser
from home.manager import *
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    is_suscribed = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 


class Contact(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)  # Assuming a maximum of 15 characters for a phone number
    query = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Contact Us Request"
        verbose_name_plural = "Contact Requests"
