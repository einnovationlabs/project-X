from django.shortcuts import render
from django.http import HttpResponse
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
    user = user_dao.get_user(user_id = user_id)
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
# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints

# Data Submission Endpoints
# Visualization Endpoints
# Data Download and Export Endpoints
# Search and Filtering Endpoints