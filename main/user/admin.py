from django.contrib import admin
from .models import Dataset, Dataset_File, Dataset_Addt_File, Dataset_Tag, Dataset_Comment, Dataset_Metadata
from .models import User, User_Profile, User_Role
from .models import Organization, Organization_Category, Organization_Profile
from .models import Organization_AdminUser, Dataset_DatasetFile, Dataset_DatasetTag, Organization_OrganizationCategory, User_UserRole

# Register your models here.
admin.site.register(Dataset)
admin.site.register(Dataset_File)
admin.site.register(Dataset_Addt_File)
admin.site.register(Dataset_Tag)
admin.site.register(Dataset_Comment)
admin.site.register(Dataset_Metadata)


admin.site.register(User)
admin.site.register(User_Profile)
admin.site.register(User_Role)


admin.site.register(Organization)
admin.site.register(Organization_Category)
admin.site.register(Organization_Profile)


admin.site.register(Organization_AdminUser)
admin.site.register(Dataset_DatasetFile)
admin.site.register(Dataset_DatasetTag)
admin.site.register(Organization_OrganizationCategory)
admin.site.register(User_UserRole)






