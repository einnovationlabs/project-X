"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from organization.models import Organization
from organization.models import OrganizationCategory
from user.user_dao import get_user


def create_org(org_data, admin_id):
    """
    Creates and Returns Organization given org_data
    """

    org = Organization(
            organization_name = org_data.get('organization_name'), 
            location = org_data.get('location'), 
            address = org_data.get('address'), 
            phone_number = org_data.get('phone_number'), 
            email = org_data.get('email'), 
            password = org_data.get('password'), 
            description = org_data.get('description'), 
            )
    org.save()

    admin = get_user(admin_id)
    org.admins.add(admin)

    for org_type in org_data.get("categories"):
        org_category = OrganizationCategory(
            type = org_type
            )
        org_category.save()
        org.categories.add(org_category)


    return org


def update_org(org_id, org_data):
    """
    Updates and Returns Organization given org_id and org_data
    """
    org = Organization.objects.get(id = org_id)

    org.organization_name = org_data.get('organization_name')
    org.location = org_data.get('location')
    org.address = org_data.get('address')
    org.phone_number = org_data.get('phone_number')
    org.email = org_data.get('email')
    org.password = org_data.get('password')
    org.description = org_data.get('description')

    org.save()

    return org


def delete_org(org_id):
    """
    Deletes and Returns Organization given org_id
    """
    org = Organization.objects.get(id = org_id)
    org.is_deleted = True
    org.save()
    return org


def get_org(org_id):
    """
    Retrieves and Returns Organization given org_id
    """
    org = Organization.objects.get(id = org_id)
    return org


def add_category(org_id):
    """
    """


def remove_category(org_id):
    """
    """


def add_org_member(admin_id, org_data):  #TODO: add member or members
    """
    Adds member to organization by user
    """
    org = get_org(org_data.get("org_id"))
    admin = org.admins.filter(admin = get_user(admin_id)).first()

    if not admin:
        return False, admin
    
    member_id = org_data.get("member_id")
    member = get_user(member_id)
    org.members.add(member)

    #TODO: reconsider roles field for user

    org.save()

    return True, org


def remove_org_member(admin_id, org_data):
    """
    Removes member from organization by user
    """
    org = get_org(org_data.get("org_id"))

    admin = org.admins.filter(admin = get_user(admin_id)).first()
    if not admin:
        return False, admin
    member_id = org_data.get("member_id")
    member = get_user(member_id)
    org.members.remove(member)

    org.save()

    return True, org

def approve_org():
    """
    Approve organization by user
    """


def disapprove_org():
    """
    Disapprove organization by user
    """