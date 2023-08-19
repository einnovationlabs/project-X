"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import User
from user.models import Role
from dataset.models import Tag
from dataset.models import File



def create_user(user_data):
    """
    Creates and Returns given user_data
    """
    try:
        user = User( 
                phone_number = user_data.get('phone_number'),
                profile_pic = user_data.get('profile_pic'),
                background_pic = user_data.get("background_pic"),
                username = user_data.get("username"),
                password_digest = user_data.get("password"),
                firstname = user_data.get("firstname"),
                lastname = user_data.get("lastname"),
                email = user_data.get("email"),
                about = user_data.get("about")
                )
        user.save()

        # LOGIC when the role is already created

        role = Role()
        role.save()
        user.roles.add(role)

        #become org_contributor on creation
        #become org admin on addition or creation of org
        #become super admin ???
        for role_name in user_data.get("roles"):
            try:
                role = Role.objects.get(name = role_name)
            except:
                role = Role(role = role_name)
            role.save()
            user.roles.add(role)

        for tag_name in user_data.get("tags"):
            try:
                tag = Tag.objects.get(name = tag_name)
            except:
                tag = Tag(name = tag_name) 
            tag.save()
            user.tags.add(tag)


        for title, url in user_data.get("files"):
            file = File(title = title, url = url)
            file.save()
            user.files.add(file)

        user.save()
    except:
        return False, "Email is already taken"
    
    return True, user


def update_user(user_id, user_data):
    """
    Updates and Returns User given user_id and user_data
    """
    exists, user = get_user(user_id)

    if not exists:
        return False, user
    
    try:
        user.firstname = user_data.get('firstname')
        user.lastname = user_data.get('lastname')
        user.username = user_data.get('username')
        user.password_digest = user_data.get('password')
        user.about = user_data.get('about')
        user.email = user_data.get('email')
        user.phone_number = user_data.get('phone_number')
        user.profile_pic = user_data.get('profile_pic')
        user.background_pic = user_data.get('background_pic')

        user.save()
    except:
        return False, "Email already taken"
    return True, user

#TODO: add user role and remove user role
def delete_user(user_id):
    """
    Deletes and Returns User given user_id
    """
    exists, user = get_user(user_id)

    if not exists:
        return False, user
    
    user.is_deleted = True
    user.save()
    return True, user


def get_user(user_id):
    """
    Retrieves and Returns User given user_id
    """
    user = User.objects.get(id = user_id)

    if not user:
        return False, user
    
    return True, user


def create_tag(user_id, tag_data):
    """
    Creates and Returns Tag given user_id
    """
    success, user = get_user(user_id)

    if not success:
        return False, None
    tag_name = tag_data.get("name")
    try:
        tag = Tag.objects.get(name = tag_name)
    except:
        tag = Tag(name = tag_name)
    tag.save()
    user.tags.add(tag)
    user.save()

    return True, tag

def get_tag(tag_id):
    """
    Retrieves and Returns Tag given tag_id
    """
    tag = Tag.objects.get(id = tag_id)

    if not tag:
        return False, tag

    return True, tag


def delete_tag(tag_id, user_id):
    """
    Deletes and Returns Tag given user_id
    """
    success, user = get_user(user_id)

    if not success:
        return False, None
    
    success, tag = get_tag(tag_id)

    if not success:
        return False, None
    user.tags.remove(tag)

    user.save()

    return True, tag


