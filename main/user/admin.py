from django.contrib import admin
from .models import User, Organization, Dataset, Dataset_File, Dataset_Additional_Info, UserOrganization

# Register your models here.
admin.site.register(User)
admin.site.register(Organization)
admin.site.register(Dataset)
admin.site.register(Dataset_File)
admin.site.register(Dataset_Additional_Info)
admin.site.register(UserOrganization)



