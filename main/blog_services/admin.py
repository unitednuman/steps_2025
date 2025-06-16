from django.contrib import admin
from .models import Articles, Reporter, Publisher

admin.site.register(Articles)
admin.site.register(Reporter)
admin.site.register(Publisher)
# Register your models here.
