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

    # owner_organization = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, default=None)
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None)

    csv_file_url = models.URLField(null= True)
    dataset_addt_files = models.ForeignKey(
        "DatasetAddtFile",
        on_delete= models.RESTRICT,
        null= True
    )

    dataset_metadata = models.ForeignKey("DatasetMetadata", on_delete=models.RESTRICT, default=None, unique= True, null=True)

    tags = models.ManyToManyField("DatasetTag", through= "Dataset_DatasetTag")


    def serialize(self):
        """
        Serializes a Dataset object
        """
        return {
            "id" : self.id,
            "is_verified" : self.is_verified,
            "addt_info" : self.addt_info,
            "tags" : [tag.serialize() for tag in self.tags.all()]
        }


class DatasetAddtFile(models.Model):
    """
    Dataset Additional Info model
    """
    title = models.CharField(max_length=50)
    file_url = models.URLField()


class DatasetTag(models.Model):
    """
    Dataset Tag model
    """
    name = models.CharField(max_length=50)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name
        }


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

class Dataset_DatasetTag(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
    DatasetTag = models.ForeignKey(DatasetTag, on_delete=models.RESTRICT)