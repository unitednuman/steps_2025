from django.db import models
from django.conf import settings

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=100, blank=False, null=False)

class Publisher(models.Model):
    company_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    address = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.SET_NULL, null=True )
    publisher = models.ManyToManyField(Publisher)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True )
