from user.models import User

def create_user(user):

    user = User(firstname = user.get('firstname'), 
            lastname = user.get('lastname'), 
            username = user.get('username'),
            password = user.get('password'),
            about = user.get('about'),
            email = user.get('email'),
            phone_number = user.get('phone_number'),
            profile_pic = user.get('profile_pic')
            )
    
    
    user.save()

    return user