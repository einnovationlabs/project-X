from django.contrib import admin
from .models import Dataset, DatasetAddtFile, DatasetTag, DatasetComment, DatasetMetadata

# Register your models here.


admin.site.register(Dataset)
admin.site.register(DatasetAddtFile)
admin.site.register(DatasetTag)
admin.site.register(DatasetComment)
admin.site.register(DatasetMetadata)