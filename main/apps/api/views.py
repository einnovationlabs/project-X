from django.shortcuts import render
import json


# Test endpoint
def home(request):
    return render(request, "pages/homepage.html")
