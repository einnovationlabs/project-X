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
    

class UserProfile(models.Model):
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


class UserRole(models.Model):
    """
    User role model
    """
    profile_user = models.BooleanField(default= True)
    org_contributor = models.BooleanField(default=False)
    org_admin = models.BooleanField(default=False)
    super_admin = models.BooleanField(default=False)



# class Organization_AdminUser(models.Model):
#     org_admin_id = models.ForeignKey(Organization, on_delete=models.RESTRICT)
#     user_id = models.ForeignKey(User, on_delete=models.RESTRICT)

#     # Add any extra fields or attributes you want for this relationship
#     # extra_field = models.CharField(max_length=100)


# class Dataset_DatasetFile(models.Model):
#     dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
#     DatasetFile = models.ForeignKey(DatasetFile, on_delete=models.RESTRICT)


# class Dataset_DatasetTag(models.Model):
#     dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
#     DatasetTag = models.ForeignKey(DatasetTag, on_delete=models.RESTRICT)


# class Organization_OrganizationCategory(models.Model):
#     organization = models.ForeignKey(Organization, on_delete=models.RESTRICT)
#     OrganizationCategory = models.ForeignKey(OrganizationCategory, on_delete=models.RESTRICT)


# class User_UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.RESTRICT)
#     UserRole = models.ForeignKey(UserRole, on_delete=models.RESTRICT)





