from django.db import models

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = models.CharField(max_length=100, blank=False, null=False)

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.SET_NULL, null=True )
