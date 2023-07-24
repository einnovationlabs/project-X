from django.db import models

# Create your models here.


class Dataset(models.Model):
    """
    Dataset model
    """
    is_publish = models.BooleanField(default= True)
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
    is_public = models.BooleanField()
    #tags = models # from frontend? thinking of many many relation for backend
    csv_data_file = models.CharField(max_length=100)
    #other_data_files =  # thinking of many to many relation


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
    tags_ids = # one to many

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


    












