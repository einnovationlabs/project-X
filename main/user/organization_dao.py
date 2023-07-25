"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import Organization

def create_org(org_data):

    org = org(firstname = org_data.get('firstname'), 
            lastname = org_data.get('lastname'), 
            orgname = org_data.get('orgname'),
            password = org_data.get('password'),
            about = org_data.get('about'),
            email = org_data.get('email'),
            phone_number = org_data.get('phone_number'),
            profile_pic = org_data.get('profile_pic')
            )
    
    
    org.save()

    return org



def update_org(org_id, org_data):

    org = org.objects.get(id = org_id)

    org.firstname = org_data.get('firstname')
    org.lastname = org_data.get('lastname')
    org.orgname = org_data.get('orgname')
    org.password = org_data.get('password')
    org.about = org_data.get('about')
    org.email = org_data.get('email')
    org.phone_number = org_data.get('phone_number')
    org.profile_pic = org_data.get('profile_pic')

    org.save()

    return org


def delete_org(org_id):
    org = org.objects.get(id = org_id)
    org.is_active = False
    org.save()
    return org