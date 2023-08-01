from django.shortcuts import render
from django.http import HttpResponse
import organization.organization_dao as organization_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.


# Organization Management endpoints
@csrf_exempt
def create_org(request, admin_id):
    """
    Endpoint to create organization
    """
    data = json.loads(request.body)

    # perform validation
    org = organization_dao.create_org(data, admin_id)
    
    return JsonResponse(org.serialize())

@csrf_exempt
def delete_org(request, org_id):
    """
    Endpoint to delete organization by id
    """
    org = organization_dao.delete_org(org_id)
    return JsonResponse(org.serialize())

@csrf_exempt
def update_org(request, org_id):
    """
    Endpoint to update organization by id
    """
    data = json.loads(request.body)
    org = organization_dao.update_org(org_id, data)

    return JsonResponse(org.serialize())

@csrf_exempt
def get_org(request, org_id):
    """
    Endpoint to get organization by id
    """
    org = organization_dao.get_org(org_id)
    return JsonResponse(org.serialize())
