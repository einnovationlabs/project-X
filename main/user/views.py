from django.shortcuts import render
from django.http import HttpResponse
import user.user_dao as user_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

def success_response(data):
    return JsonResponse(data)

def failure_response(message):
    return JsonResponse({"message" : message})

# Test endpoint
def home(request):
    return HttpResponse('Hello world')

# User Management Endpoints
@csrf_exempt
def update_user_role(request, user_id):
    """
    Endpoint to update user roles
    """
    data = json.loads(request.body)

    success, user_roles = user_dao.update_user_role(user_id, data)

    if not success:
        return 

    return JsonResponse(user_roles)


@csrf_exempt
def create_user(request):
    """
    Endpoint to create user
    """
    data = json.loads(request.body)

    # perform validation
    created, user = user_dao.create_user(data)

    if not created:
        return failure_response("Failed to create user")
    
    return success_response(user.serialize())


@csrf_exempt
def delete_user(request, user_id):
    """
    Endpoint to delete user by id
    """
    deleted, user = user_dao.delete_user(user_id)

    if not deleted:
        return failure_response("Failed to delete user")
    
    return success_response(user.serialize())


@csrf_exempt
def update_user(request, user_id):
    """
    Endpoint to update user by id
    """
    data = json.loads(request.body)
    updated, user = user_dao.update_user(user_id, data)

    if not updated:
        return failure_response("Failed to update user")
    
    return success_response(user.serialize())


@csrf_exempt
def get_user(request, user_id):
    """
    Endpoint to get user by id
    """
    success, user = user_dao.get_user(user_id = user_id)

    if not success:
        return failure_response("Failed to get user")
    
    return success_response(user.serialize())


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