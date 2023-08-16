from django.shortcuts import render
from django.http import HttpResponse
from dataset.models import Dataset
import dataset.dataset_dao as dataset_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
import dataset.dataset_dao as dataset_dao
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

# Test endpoint
def home(request):
    return HttpResponse('Hello world')

##### DATASETS ENDPOINTS #####
@csrf_exempt
def create_dataset(request, user_id):
    """
    Endpoint to create dataset
    """
    data = json.loads(request.body)

    dataset = dataset_dao.create_dataset(data, user_id)
    
    return JsonResponse(dataset)


@csrf_exempt
def delete_dataset(request, dataset_id):
    """
    Endpoint to delete dataset by id
    """
    dataset = dataset_dao.delete_dataset(dataset_id)
    return JsonResponse(dataset.serialize())

@csrf_exempt
def update_dataset(request, dataset_id):
    """
    Endpoint to update dataset by id
    """
    data = json.loads(request.body)
    dataset = dataset_dao.update_dataset(dataset_id, data)

    return JsonResponse(dataset.serialize())


@csrf_exempt
def get_dataset(request, dataset_id):
    """
    Endpoint to get dataset by id
    """
    dataset = dataset_dao.get_dataset(dataset_id = dataset_id)
    return JsonResponse(dataset)

@csrf_exempt
def get_all_datasets(request):
    """
    Endpoint to get all datasets
    """
    datasets = dataset_dao.get_all_datasets()

    return JsonResponse(datasets)

@csrf_exempt
def delete_file(request, user_id):
    """
    Endpoint to delete file 
    """
    file_id = json.loads(request.body).get("file_id")
    return JsonResponse(dataset_dao.delete_file(user_id, file_id))

@csrf_exempt
def create_file(request, user_id):
    """
    Endpoint to delete file 
    """
    file_data = json.loads(request.body)
    return JsonResponse(dataset_dao.create_file(user_id, file_data))
    
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

# Comment endpoints

@csrf_exempt
def create_comment(request, user_id):
    """
    Endpoint to create comment
    """
    data = json.loads(request.body)

    comment = dataset_dao.create_comment(user_id, data)
    
    return JsonResponse(comment)


@csrf_exempt
def delete_comment(request, user_id):
    """
    Endpoint to delete file 
    """
    comment_id = json.loads(request.body).get("comment_id")
    return JsonResponse(dataset_dao.delete_comment(user_id, comment_id))

# Like endpoints

@csrf_exempt
def create_like(request, user_id):
    """
    Endpoint to create like
    """
    data = json.loads(request.body)

    comment = dataset_dao.create_like(user_id, data)
    
    return JsonResponse(comment)


@csrf_exempt
def delete_like(request, user_id):
    """
    Endpoint to delete like 
    """
    like_id = json.loads(request.body).get("like_id")
    return JsonResponse(dataset_dao.delete_like(user_id, like_id))


# Bookmark endpoints

@csrf_exempt
def create_bookmark(request, user_id):
    """
    Endpoint to create bookmark
    """
    data = json.loads(request.body)

    comment = dataset_dao.create_bookmark(user_id, data)
    
    return JsonResponse(comment)


@csrf_exempt
def delete_bookmark(request, user_id):
    """
    Endpoint to delete bookmark 
    """
    bookmark_id = json.loads(request.body).get("bookmark_id")
    return JsonResponse(dataset_dao.delete_bookmark(user_id, bookmark_id))


# TODO: Data Submission Endpoints
# TODO: Visualization Endpoints
# TODO: Data Download and Export Endpoints

# TODO: Data Submission Endpoints
# TODO: Visualization Endpoints
# TODO: Data Download and Export Endpoints
# TODO: Search and Filtering Endpoints