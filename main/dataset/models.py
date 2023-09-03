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


    is_published = models.BooleanField(default=False)
    is_archived = models.BooleanField(default= False)
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    title = models.CharField(max_length= 100, default="")  

    description = models.CharField(max_length= 1000, default="")  

    status = models.TextField(default=None)  #make it choices

    addt_info = models.TextField(default=None)

    owner_organization = models.ForeignKey("organization.Organization", on_delete=models.RESTRICT, default=None, null=True)
    owner_user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None)


    metadata = models.ForeignKey("Dataset_Metadata", on_delete=models.RESTRICT, unique= True, blank= False)
    
    tags = models.ManyToManyField("Tag",  through="Dataset_Tag")
    files = models.ManyToManyField("File", through="Dataset_File")

    def serialize(self):
        """
        Serializes a Dataset object
        """
        return {
            "id" : self.id,
            "is_verified" : self.is_verified,
            "has_user_policy" : self.has_user_policy,
            "is_government" : self.is_government,
            "is_public" : self.is_public,
            "is_published" : self.is_published,
            "is_archived" : self.is_archived,
            "is_approved" : self.is_approved,
            "title": self.title,
            "description": self.description,
            "status" : self.status,
            "is_deleted" : self.is_deleted,
            "addt_info" : self.addt_info,
            "owner_user" : self.owner_user.serialize() if self.owner_user else None,
            "owner_organization" : self.owner_organization.serialize() if self.owner_organization else None,
            "metadata" : self.metadata.serialize(),
            
            "tags" : [tag.serialize() for tag in self.tags.all()],
            "files" : [file.serialize() for file in self.files.all()],

            "bookmarks" : [bookmark.serialize() for bookmark in self.dataset_bookmarks.all()],
            "likes" : [like.serialize() for like in self.dataset_likes.all()],
            "comments" : [comment.serialize() for comment in self.dataset_comments.all()]

        }

    
class File(models.Model):
    """
    File model
    """
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default= None, blank=False)
    status = models.BooleanField(default=True)


    def serialize(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "url" : self.url,
            "status" : self.status,
        }
    

class Dataset_File(models.Model):
    files = models.ForeignKey("File", on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)



# TODO: consider situation where orgs and users are also tagged
# TODO: name and type of that tag
# TODO: users, organizations should have files as well/relationships
# TODO: likes table 


class Comment(models.Model):
    """
    Dataset Comment model
    """
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    
    status = models.BooleanField(default=True)

    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT, related_name="dataset_comments", default=None)
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT, related_name="user_comments", default=None) 

    def serialize(self):
        return {
            "id" : self.id,
            "body" : self.body,
            "status" : self.status,
            "data_created" : self.dataset,
            "dataset" :self.dataset.id,
            "user" : self.user.id
        }


class Dataset_Metadata(models.Model):
    """
    Metadata model
    """
    metadata_file = models.CharField(max_length= 50, null=True)  #relation with file model
    metadata_blurb = models.CharField(max_length= 1000, blank= True, null= True)
    metadata_source_link = models.URLField()
    metadata_resource_type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)  # user or org or Admin ?
    maintainer = models.CharField(max_length=100)  # user or org or Admin ?
    license_link = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def serialize(self):
        return {
            "id" : self.id,
            "file" : self.file,
            "date_created" : self.date_created,
            "date_modified" : self.date_modified
        }
    

class Tag(models.Model):
    """
    Tag model
    """
    name = models.CharField(max_length=50, unique=True)

    #TODO: consider unique together here
    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name
        }
    
class Dataset_Tag(models.Model):
    tags = models.ForeignKey("Tag",  on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)


class Like(models.Model):
    """
    Like model
    """
    status = models.BooleanField(default=True)
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None, related_name="user_likes")
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT, related_name="dataset_likes", default=None)

    class Meta:
        unique_together = ("user", "dataset")

    def serialize(self):
        return {
            "id" : self.id,
            "status" : self.status,
            "user" : self.user.id,
            "dataset" : self.dataset.id
        }


class Bookmark(models.Model):
    """
    Bookmark model
    """
    status = models.BooleanField(default=True)
    user = models.ForeignKey("user.User", on_delete=models.RESTRICT, default=None, related_name="user_bookmarks")
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT, related_name="dataset_bookmarks", default=None)

    class Meta:
        unique_together = ("user", "dataset")

    def serialize(self):
        return {
            "id" : self.id,
            "status" : self.status,
            "user" : self.user.id,
            "dataset" : self.dataset.id
        }




