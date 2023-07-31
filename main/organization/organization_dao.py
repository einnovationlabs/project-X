"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from models import Organization
from models import OrganizationProfile
from models import OrganizationCategory

def create_org(org_data):
    """
    Creates and Returns Organization given org_data
    """
    org = Organization()
    org.save()

    org_profile = OrganizationProfile(
            org_name = org_data.get("profile").get('organization_name'), 
            location = org_data.get("profile").get('location'), 
            address = org_data.get("profile").get('address'), 
            phone_number = org_data.get("profile").get('phone_number'), 
            email = org_data.get("profile").get('email'), 
            password = org_data.get("profile").get('password'), 
            description = org_data.get("profile").get('description'), 
            )
    org_profile.save()

    org_category = OrganizationCategory(
        type = org_data.get("category").get("type")
    )

    org_category.save()
    return org


def update_org(org_id, org_data):
    """
    Updates and Returns Organization given org_id and org_data
    """
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
    """
    Deletes and Returns Organization given org_id
    """
    org = org.objects.get(id = org_id)
    org.is_active = False
    org.save()
    return org


def get_org(org_id):
    """
    Retrieves and Returns Organization given org_id
    """