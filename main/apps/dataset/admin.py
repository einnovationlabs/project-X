from django.contrib import admin

from .models import (Bookmark, Comment, Dataset, Dataset_File,
                     Dataset_Metadata, Dataset_Tag, File, Like, Tag)

# Register your models here.

admin.site.register(Dataset)
admin.site.register(File)
admin.site.register(Dataset_File)
admin.site.register(Comment)
admin.site.register(Dataset_Metadata)
admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(Dataset_Tag)
admin.site.register(Tag)
