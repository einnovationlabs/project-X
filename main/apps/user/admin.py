from django.contrib import admin
from .models import User, Role, User_Role, User_File, User_Tag

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(User_Role)
admin.site.register(User_Tag)
admin.site.register(User_File)
