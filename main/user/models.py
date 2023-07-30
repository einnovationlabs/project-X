from django.db import models

# Create your models here.
class User(models.Model):
    """
    User model
    """
    phone_number = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=100, blank=True, null= True)
    background_pic = models.CharField(max_length=100, blank=True, null= True)
    is_deleted = models.BooleanField(default= True)


    def serialize(self):

        return {
            "phone_number" : self.phone_number,
            "profile_picture" : self.profile_pic,
            "background_picture" : self.background_pic,
            "is_deleted" : self.is_deleted
        }
    

class User_Profile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, unique=True, on_delete=models.RESTRICT)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length= 50)
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    email = models.EmailField()
    about = models.CharField(max_length= 1000, blank= True, null= True)


class User_Role(models.Model):
    """
    User role model
    """
    profile_user = models.BooleanField(default= True)
    org_contributor = models.BooleanField(default=False)
    org_admin = models.BooleanField(default=False)
    super_admin = models.BooleanField(default=False)


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

    owner_organization = models.ForeignKey("Organization", on_delete=models.RESTRICT, default=None)
    owner_user = models.ForeignKey("User", on_delete=models.RESTRICT, default=None)



class Dataset_File(models.Model):
    """
    Dataset File model
    """
    file_url = models.URLField()


class Dataset_Addt_File(models.Model):
    """
    Dataset Additional Info model
    """
    title = models.CharField(max_length=50)
    file_url = models.URLField()

    dataset_file = models.ForeignKey(
        "Dataset_File",
        on_delete=models.RESTRICT
    )


class Dataset_Tag(models.Model):
    """
    Dataset Tag model
    """
    name = models.CharField(max_length=50)


class Dataset_Comment(models.Model):
    """
    Dataset Comment model
    """
    dataset = models.ForeignKey("Dataset", on_delete=models.RESTRICT)
    user = models.ForeignKey("User", on_delete=models.RESTRICT)

    body = models.TextField()


class Dataset_Metadata(models.Model):
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


class Organization(models.Model):
    """
    Organization model
    """

    def serialize(self):
        """
        Serializes Organization object
        """
        return {
            "organization name" : self.organization_name,
            "phone_number" : self.phone_number,
            "description" : self.description,
            "category" : self.category,
            "email" : self.email,
            "location" : self.location,
            "address" : self.address,
            "is_deleted" : self.is_deleted
        }


class Organization_Category(models.Model):
    """
    Organization Category model
    """
    type = models.CharField(max_length=50)


class Organization_Profile(models.Model):
    """
    Organization Profile model
    """
    organization = models.OneToOneField(Organization, unique=True, on_delete=models.RESTRICT)
    organization_name = models.CharField(max_length= 100)
    location = models.CharField(max_length= 100)
    address = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length= 50)
    description = models.CharField(max_length= 1000, blank= True, null= True)
    is_deleted = models.BooleanField(default= True)


class Organization_AdminUser(models.Model):
    org_admin_id = models.ForeignKey(Organization, on_delete=models.RESTRICT)
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)

    # Add any extra fields or attributes you want for this relationship
    # extra_field = models.CharField(max_length=100)


class Dataset_DatasetFile(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
    dataset_file = models.ForeignKey(Dataset_File, on_delete=models.RESTRICT)


class Dataset_DatasetTag(models.Model):
    dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
    dataset_tag = models.ForeignKey(Dataset_Tag, on_delete=models.RESTRICT)


class Organization_OrganizationCategory(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.RESTRICT)
    organization_category = models.ForeignKey(Organization_Category, on_delete=models.RESTRICT)


class User_UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    user_role = models.ForeignKey(User_Role, on_delete=models.RESTRICT)





