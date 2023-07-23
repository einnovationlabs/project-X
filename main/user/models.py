from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length= 50)
    firstname = models.CharField(max_length= 100)
    lastname = models.CharField(max_length= 100)
    about = models.CharField(max_length= 1000, blank= True, null= True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    profile_pic = models.CharField(max_length=100, blank=True, null= True)
    is_active = models.BooleanField(default= True)


    def serialize(self):

        return {
            "firstname" : self.firstname,
            "lastname" : self.lastname,
            "username" : self.username,
            "email" : self.email,
            "is_active" : self.is_active
        }




