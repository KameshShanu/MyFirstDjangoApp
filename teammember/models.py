from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from phone_field import PhoneField

# Create your models here.
class Teammember(models.Model):

    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    is_Regular = models.BooleanField("Regular", default=False)
    is_Admin = models.BooleanField("Admin", default=False)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.firstName