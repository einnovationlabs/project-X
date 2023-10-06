from django.contrib import admin

from .models import (
    DatasetBookmark,
    DatasetComment,
    Dataset,
    Dataset_DatasetFile,
    DatasetMetadata,
    Dataset_DatasetTag,
    DatasetFile,
    DatasetLike,
    DatasetTag,
)

# Register your models here.

admin.site.register(Dataset)
admin.site.register(DatasetFile)
admin.site.register(Dataset_DatasetFile)
admin.site.register(DatasetComment)
admin.site.register(DatasetMetadata)
admin.site.register(DatasetLike)
admin.site.register(DatasetBookmark)
admin.site.register(Dataset_DatasetTag)
admin.site.register(DatasetTag)
