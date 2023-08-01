from django.db import models


# Create your models here.
class User(models.Model):
    """
    User model
    """
    phone_number = models.CharField(max_length=50, null=True)
    profile_pic = models.CharField(max_length=100, blank=True, null= True)
    background_pic = models.CharField(max_length=100, blank=True, null= True)
    username = models.CharField(max_length = 100, null=True)
    password = models.CharField(max_length= 50, null=True)
    firstname = models.CharField(max_length= 100, null=True)
    lastname = models.CharField(max_length= 100, null=True)
    email = models.EmailField(null= True)
    about = models.CharField(max_length= 1000, blank= True, null= True)
    is_deleted = models.BooleanField(default= False)


    def serialize(self):

        return {
            "id":  self.id,
            "phone_number" : self.phone_number,
            "profile_picture" : self.profile_pic,
            "background_picture" : self.background_pic,
            "is_deleted" : self.is_deleted
        }


class UserRole(models.Model):
    """
    User role model
    """
    profile_user = models.BooleanField(default= True)
    org_contributor = models.BooleanField(default=False)
    org_admin = models.BooleanField(default=False)
    super_admin = models.BooleanField(default=False)





#     # Add any extra fields or attributes you want for this relationship
#     # extra_field = models.CharField(max_length=100)


# class Dataset_DatasetFile(models.Model):
#     dataset = models.ForeignKey(Dataset, on_delete=models.RESTRICT)
#     DatasetFile = models.ForeignKey(DatasetFile, on_delete=models.RESTRICT)




# class User_UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.RESTRICT)
#     UserRole = models.ForeignKey(UserRole, on_delete=models.RESTRICT)





