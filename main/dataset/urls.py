from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('orgs/', views.create_dataset, name = "create_dataset"),
    path('orgs/get/<int:dataset_id>/', views.get_dataset, name = "get_dataset"),
    path('orgs/delete/<int:dataset_id>/', views.delete_dataset, name = "delete_dataset"),
    path('orgs/update/<int:dataset_id>/', views.update_dataset, name = "update_dataset"),

]