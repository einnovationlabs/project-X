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
def create_dataset(request):
    """
    Endpoint to create dataset
    """
    data = json.loads(request.body)

    dataset = dataset_dao.create_dataset(data)
    
    return JsonResponse(dataset.serialize())


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
    dataset = dataset_dao.get_dataset(dataset_id = dataset_id)
    return JsonResponse(dataset.serialize())

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