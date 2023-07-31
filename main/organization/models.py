from django.db import models

# Create your models here.
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


class OrganizationCategory(models.Model):
    """
    Organization Category model
    """
    type = models.CharField(max_length=50)


class OrganizationProfile(models.Model):
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
