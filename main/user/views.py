from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
import crud

# Create your views here.

def home(request):
    return HttpResponse('Hello world')


def create_user(request):

    body = request.data

    # perform validation
    user = crud.create_user(body)
    
    return HttpResponse(user)

def delete_user(request, id):
    user = User.objects.get(id = id)
    user.delete()


def update_user(request, id):
    body = request.data
    user = User.objects.get(id = id)
    user.firstname = body.get('firstname')
    user.lastname = body.get('lastname')
    user.username = body.get('username')
    user.password = body.get('password')
    user.about = body.get('about')
    user.email = body.get('email']
    user.phone_number = body.get('phone_number']
    user.profile_pic = body.get('profile_pic']

    user.save()
    return user

def get_user(request):
    user = User.objects.get(id = id)
    return HttpResponse(user)

