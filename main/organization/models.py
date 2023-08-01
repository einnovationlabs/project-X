from django.db import models

# Create your models here.
class Organization(models.Model):
    """
    Organization model
    """
    organization_name = models.CharField(max_length= 100, default=None)
    location = models.CharField(max_length= 100, default=None)
    address = models.CharField(max_length= 100, default=None)
    phone_number = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(max_length= 50, default=None)
    description = models.CharField(max_length= 1000, blank= True, null= True)
    is_deleted = models.BooleanField(default= True)
    category = models.ManyToManyField("OrganizationCategory", through= "Organization_OrganizationCategory")



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


class Organization_OrganizationCategory(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.RESTRICT)
    organizationCategory = models.ForeignKey(OrganizationCategory, on_delete=models.RESTRICT)