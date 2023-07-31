from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
import user.user_dao as user_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.


# Organization Management endpoints
@csrf_exempt
def create_org(request):
    """
    Endpoint to create organization
    """

@csrf_exempt
def delete_org(request, org_id):
    """
    Endpoint to delete organization by id
    """

@csrf_exempt
def update_org(reques, org_id):
    """
    Endpoint to update organization by id
    """

@csrf_exempt
def get_org(request, org_id):
    """
    Endpoint to get organization by id
    """
