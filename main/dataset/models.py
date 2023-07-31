from django.db import models

# Create your models here.


class Dataset(models.Model):
    """
    Dataset model
    """
    is_verified = models.BooleanField(default= False)
    has_user_policy = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    status = models.TextField(default=None)  #make it choices

    addt_info = models.TextField(default=None)

    number_of_likes = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    owner_organization = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, default=None)
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None)



class DatasetFile(models.Model):
    """
    Dataset File model
    """
    file_url = models.URLField()


class DatasetAddtFile(models.Model):
    """
    Dataset Additional Info model
    """
    title = models.CharField(max_length=50)
    file_url = models.URLField()

    DatasetFile = models.ForeignKey(
        "DatasetFile",
        on_delete=models.RESTRICT
    )


class DatasetTag(models.Model):
    """
    Dataset Tag model
    """
    name = models.CharField(max_length=50)


class DatasetComment(models.Model):
    """
    Dataset Comment model
    """
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT)

    body = models.TextField()


class DatasetMetadata(models.Model):
    """
    Dataset Metadata model
    """
    dataset = models.OneToOneField(Dataset, on_delete=models.RESTRICT)

    metadata_file = models.URLField(null=True)
    metadata_title = models.CharField(max_length= 100)  
    metadata_blurb = models.CharField(max_length= 1000, blank= True, null= True)
    metadata_source_link = models.URLField()
    metadata_resource_type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)  # user or org or Admin ?
    maintainer = models.CharField(max_length=100)  # user or org or Admin ?
    license_link = models.URLField()
    date_created = models.DateField( auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
