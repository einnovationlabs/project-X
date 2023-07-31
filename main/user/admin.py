from django.contrib import admin
from .models import User, UserProfile, UserRole
# from .models import Organization_AdminUser, Dataset_DatasetFile, Dataset_DatasetTag, Organization_OrganizationCategory, User_UserRole

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserRole)


# admin.site.register(Organization_AdminUser)
# admin.site.register(Dataset_DatasetFile)
# admin.site.register(Dataset_DatasetTag)
# admin.site.register(Organization_OrganizationCategory)
# admin.site.register(User_UserRole)






