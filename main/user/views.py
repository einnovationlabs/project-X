from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
import user.user_dao as user_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

# Test endpoint
def home(request):
    return HttpResponse('Hello world')

# User Management Endpoints
@csrf_exempt
def create_user(request):
    """
    Endpoint to create user
    """
    data = json.loads(request.body)

    # perform validation
    user = user_dao.create_user(data)
    
    return JsonResponse(user.serialize())


@csrf_exempt
def delete_user(request, user_id):
    """
    Endpoint to delete user by id
    """
    user = user_dao.delete_user(user_id)
    return JsonResponse(user.serialize())


@csrf_exempt
def update_user(request, user_id):
    """
    Endpoint to update user by id
    """
    data = json.loads(request.body)
    user = user_dao.update_user(user_id, data)
    return JsonResponse(user.serialize())


@csrf_exempt
def get_user(request, user_id):
    """
    Endpoint to get user by id
    """
    user = User.objects.get(id = user_id)
    return JsonResponse(user.serialize())


@csrf_exempt
def user_login(request):
    """
    Endpoint to login user
    """

@csrf_exempt
def user_logout(request):
    """
    Endpoint to logout user
    """

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


##### DATASETS ENDPOINTS #####
@csrf_exempt
def create_dataset(request):
    """
    Endpoint to create dataset
    """

@csrf_exempt
def delete_dataset(request, dataset_id):
    """
    Endpoint to delete dataset by id
    """

@csrf_exempt
def update_dataset(reques, dataset_id):
    """
    Endpoint to update dataset by id
    """

@csrf_exempt
def get_dataset(request, dataset_id):
    """
    Endpoint to get dataset by id
    """

@csrf_exempt
def get_all_datasets(request):
    """
    Endpoint to get all datasets
    """

# Search and Filtering Endpoints
@csrf_exempt
def search_dataset_by_category(request):
    """
    Endpoint to search datasets by category
    """

@csrf_exempt
def filter_dataset_by_source(request):
    """
    Endpoint to filter datasets by source
    """

@csrf_exempt
def filter_dataset_by_date_range(request):
    """
    Endpoint to filter datasets by date range
    """
# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints

# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints
# Search and Filtering Endpoints