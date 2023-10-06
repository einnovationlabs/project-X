from django.db import models
from datetime import datetime


class Dataset(models.Model):
    custom_single_fields = [
        "is_government",
        "is_public",
        "title",
        "description",
        "addt_info",
    ]
    __tablename__ = "Dataset"
    is_verified = models.BooleanField(default=False)
    has_user_policy = models.BooleanField(default=False)
    is_government = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)
    is_published = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=1000, default="")
    status = models.CharField(default="pending", max_length=10)
    addt_info = models.TextField(default=None)

    # Foreign Key Fields
    owner_organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.RESTRICT,
        default=None,
        null=True,
    )
    owner_user = models.ForeignKey(
        "user.User", on_delete=models.RESTRICT, default=None
    )
    metadata = models.ForeignKey(
        "DatasetMetadata", on_delete=models.RESTRICT, unique=True, blank=False
    )

    # Many-to-Many Relationships
    tags = models.ManyToManyField("Tag", through="Dataset_Tag")
    files = models.ManyToManyField("File", through="Dataset_File")

    def serialize(self):
        return {
            "id": self.id,
            "is_verified": self.is_verified,
            "has_user_policy": self.has_user_policy,
            "is_government": self.is_government,
            "is_public": self.is_public,
            "is_published": self.is_published,
            "is_archived": self.is_archived,
            "is_approved": self.is_approved,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "is_deleted": self.is_deleted,
            "addt_info": self.addt_info,
            "owner_user": f"{self.owner_user.firstname} {self.owner_user.lastname}"
            if self.owner_user
            else "",
            "owner_organization": self.owner_organization.serialize()
            if self.owner_organization
            else "",
            "metadata": self.metadata.serialize(),
            "tags": [tag.serialize() for tag in self.tags.all()],
            "files": [file.serialize() for file in self.files.all()],
            "bookmarks": [
                bookmark.serialize()
                for bookmark in self.dataset_bookmarks.all()
            ],
            "likes": [like.serialize() for like in self.dataset_likes.all()],
            "comments": [
                comment.serialize() for comment in self.dataset_comments.all()
            ],
        }


class DatasetMetadata(models.Model):
    file = models.CharField(max_length=50, null=True)
    blurb = models.CharField(max_length=1000, blank=True, null=True)
    source_link = models.URLField(null=True)
    resource_type = models.CharField(max_length=50, null=True)
    publisher = models.CharField(
        max_length=100, null=True
    )  # user or org or Admin ?
    maintainer = models.CharField(
        max_length=100, null=True
    )  # user or org or Admin ?
    license_link = models.URLField(null=True)
    date_created = models.DateField(default=datetime.today)
    date_modified = models.DateField(auto_now=True)

    def serialize(self):
        return {
            "id": self.id,
            "file": self.file,
            "date_created": self.date_created,
            "date_modified": self.date_modified,
        }


class File(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=50, default=None, blank=False)
    status = models.BooleanField(default=True)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "url": self.url,
            "status": self.status,
        }


class Dataset_File(models.Model):
    files = models.ForeignKey("File", on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)


# TODO: consider situation where orgs and users are also tagged
# TODO: name and type of that tag
# TODO: users, organizations should have files as well/relationships
# TODO: likes table


class DatasetComment(models.Model):
    body = models.TextField()
    date_created = models.DateField(default=datetime.today)
    date_modified = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_comments",
        default=None,
    )
    author = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        related_name="user_comments",
        default=None,
    )

    def serialize(self):
        return {
            "id": self.id,
            "body": self.body,
            "status": self.status,
            "data_created": self.date_created,
        }


class Tag(models.Model):
    """
    Tag model
    """

    name = models.CharField(max_length=50, unique=True)

    # TODO: consider unique together here
    def serialize(self):
        return {"id": self.id, "name": self.name}


class Dataset_Tag(models.Model):
    tags = models.ForeignKey("Tag", on_delete=models.RESTRICT)
    datasets = models.ForeignKey("Dataset", on_delete=models.RESTRICT)


class Like(models.Model):
    status = models.BooleanField(default=True)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        default=None,
        related_name="user_likes",
    )
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_likes",
        default=None,
    )

    class Meta:
        unique_together = ("user", "dataset")

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "user": self.user.id,
            "dataset": self.dataset.id,
        }


class Bookmark(models.Model):
    status = models.BooleanField(default=True)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.RESTRICT,
        default=None,
        related_name="user_bookmarks",
    )
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.RESTRICT,
        related_name="dataset_bookmarks",
        default=None,
    )

    class Meta:
        unique_together = ("user", "dataset")

    def serialize(self):
        return {
            "id": self.id,
            "status": self.status,
            "user": self.user.id,
            "dataset": self.dataset.id,
        }
