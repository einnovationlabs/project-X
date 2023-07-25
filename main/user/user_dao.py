"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import User

def create_user(user_data):

    user = User(firstname = user_data.get('firstname'), 
            lastname = user_data.get('lastname'), 
            username = user_data.get('username'),
            password = user_data.get('password'),
            about = user_data.get('about'),
            email = user_data.get('email'),
            phone_number = user_data.get('phone_number'),
            profile_pic = user_data.get('profile_pic')
            )
    
    
    user.save()

    return user



def update_user(user_id, user_data):

    user = User.objects.get(id = user_id)

    user.firstname = user_data.get('firstname')
    user.lastname = user_data.get('lastname')
    user.username = user_data.get('username')
    user.password = user_data.get('password')
    user.about = user_data.get('about')
    user.email = user_data.get('email')
    user.phone_number = user_data.get('phone_number')
    user.profile_pic = user_data.get('profile_pic')

    user.save()

    return user


def delete_user(user_id):
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return user