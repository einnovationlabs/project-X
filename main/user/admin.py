from django.contrib import admin
from .models import User, Organization, Dataset

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Dataset)


