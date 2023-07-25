from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
import user.user_dao as user_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello world')

@csrf_exempt
def create_user(request):

    data = json.loads(request.body)

    # perform validation
    user = user_dao.create_user(data)
    
    return JsonResponse(user.serialize())


@csrf_exempt
def delete_user(request, user_id):
    user = user_dao.delete_user(user_id)
    return JsonResponse(user.serialize())


@csrf_exempt
def update_user(request, user_id):
    data = json.loads(request.body)
    user = user_dao.update_user(user_id, data)
    return JsonResponse(user.serialize())


@csrf_exempt
def get_user(request, user_id):
    user = User.objects.get(id = user_id)
    return JsonResponse(user.serialize())

