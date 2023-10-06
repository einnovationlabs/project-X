from django.contrib import admin

from .models import (
    Bookmark,
    DatasetComment,
    Dataset,
    Dataset_File,
    DatasetMetadata,
    Dataset_Tag,
    File,
    Like,
    Tag,
)

# Register your models here.

admin.site.register(Dataset)
admin.site.register(File)
admin.site.register(Dataset_File)
admin.site.register(DatasetComment)
admin.site.register(DatasetMetadata)
admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(Dataset_Tag)
admin.site.register(Tag)
