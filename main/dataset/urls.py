from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('datasets/<int:owner_user_id>/', views.create_dataset, name = "create_dataset"),
    path('datasets/get/<int:dataset_id>/', views.get_dataset, name = "get_dataset"),
    path('datasets/delete/<int:dataset_id>/', views.delete_dataset, name = "delete_dataset"),
    path('datasets/update/<int:dataset_id>/', views.update_dataset, name = "update_dataset"),

]