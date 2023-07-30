"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import User
from user.models import User_Profile
from user.models import User_Role

def create_user(user_data):
    """
    Creates and Returns given user_data
    """
    user = User( 
            phone_number = user_data.get('phone_number'),
            profile_pic = user_data.get('profile_pic'),
            background_pic = user_data.get("background_pic")
            )
    
    
    user.save()
    
    user_profile = User_Profile(
        username = user_data.get("profile").get("username"),
        password = user_data.get("profile").get("password"),
        firstname = user_data.get("profile").get("firstname"),
        lastname = user_data.get("profile").get("lastname"),
        email = user_data.get("profile").get("email"),
        about = user_data.get("profile").get("about")
    )

    user_profile.save()

    user_role = User_Role(
        org_contributor = user_data.get("roles").get("organization_contributor"),
        org_admin = user_data.get("roles").get("organization_admin"),
        super_admin = user_data.get("roles").get("super_admin")
    )

    user_role.save()

    return user


def update_user(user_id, user_data):
    """
    Updates and Returns User given user_id and user_data
    """
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
    """
    Deletes and Returns User given user_id
    """
    user = User.objects.get(id = user_id)
    user.is_active = False
    user.save()
    return user


def get_user(user_id):
    """
    Retrieves and Returns User given user_id
    """
    user = User.objects.get(id = user_id)
    return user