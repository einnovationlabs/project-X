from django.contrib import admin
from .models import Dataset, File, Dataset_File, Dataset_Tag, Comment, Dataset_Metadata, Like, Bookmark, Tag

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




