from django.db import models

# Create your models here.

class Dataset_File(models.Model):
    """
    Dataset File model
    """
    file_url = models.URLField()
    user = models.ForeignKey(
        "User",
        related_name="dataset_files",
        on_delete=models.RESTRICT
    )

class Dataset_Additional_Info(models.Model):
    """
    Dataset Additional Info model
    """
    title = models.CharField(max_length=50)
    data = models.TextField()
    dataset = models.ForeignKey(
        "Dataset",
        related_name="dataset_additional_infos",
        on_delete=models.RESTRICT
    )


# class Dataset_Tag(models.Model):
#     """
#     Dataset Tag model
#     """
#     name = models.CharField(max_length=50)
#     user_id = 

class Dataset(models.Model):
    """
    Dataset model
    """
    is_published = models.BooleanField(default= True)
    metadata_file = models.URLField(null=True)
    date_created = models.DateField( auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    metadata_title = models.CharField(max_length= 100)  # create 1:1 table for metadata and dataset
    metadata_blurb = models.CharField(max_length= 1000, blank= True, null= True)
    metadata_source_link = models.URLField()
    metadata_resource_type = models.CharField(max_length=50)
    publisher = models.CharField(max_length=100)  # user or org or Admin ?
    maintainer = models.CharField(max_length=100)  # user or org or Admin ?
    license_link = models.URLField()
    is_government = models.BooleanField()
    is_public = models.BooleanField(default=False)
    csv_data_file = models.URLField()
    is_archived = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)




    # tags = models.OneToMany(to = Dataset_Tag) # from frontend? thinking of many many relation for backend


class Organization(models.Model):
    """
    Organization model
    """
    organization_name = models.CharField(max_length= 100)
    location = models.CharField(max_length= 100)
    address = models.CharField(max_length= 100)
    phone_number = models.CharField(max_length=50)
    category = models.CharField(max_length= 100)
    email = models.EmailField()
    password = models.CharField(max_length= 50)
    description = models.CharField(max_length= 1000, blank= True, null= True)
    is_active = models.BooleanField(default= True)
    # organization_admin = 


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
            "is_active" : self.is_active
        }


class User(models.Model):
    """
    User model
    """
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length= 50)
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    about = models.CharField(max_length= 1000, blank= True, null= True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=100, blank=True, null= True)
    background_pic = models.CharField(max_length=100, blank=True, null= True)
    is_active = models.BooleanField(default= True)


    datasets_ids = models.ManyToManyField(to=Dataset, related_name="datasets")  #many to many
    organizations_ids = models.ManyToManyField(to = Organization, related_name = "organizations")  #many to many

    PROFILE = "PRF"
    ORG_CONTRIBUTOR = "OCR"
    ORG_ADMIN = "OAD"
    SUPER_ADMIN = "SAD"

    USER_TYPE_CHOICES = [
        (PROFILE, "Profile User"),
        (ORG_CONTRIBUTOR, "Organization Contributor"),
        (ORG_ADMIN, "Organization Admin"),
        (SUPER_ADMIN, "Super Admin")
    ]

    user_type = models.CharField(
        max_length= 3,
        choices= USER_TYPE_CHOICES,
        default= PROFILE
    )


    def serialize(self):

        return {
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "username" : self.username,
            "email" : self.email,
            "is_active" : self.is_active
        }
    

class UserOrganization(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)








