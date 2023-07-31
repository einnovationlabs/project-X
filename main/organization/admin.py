from django.contrib import admin
from .models import Organization, OrganizationCategory, OrganizationProfile


# Register your models here.
admin.site.register(Organization)
admin.site.register(OrganizationCategory)
admin.site.register(OrganizationProfile)