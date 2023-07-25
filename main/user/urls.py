from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('users/get/<int:user_id>/', views.get_user, name='get_user'),
    path('users/', views.create_user, name='create_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),

    path('orgs/', views.create_org, name = "create_org"),
    path('orgs/get/<int:org_id>/', views.get_org, name = "get_org"),
    path('orgs/delete/<int:org_id>/', views.delete_org, name = "delete_org"),
    path('orgs/update/<int:org_id>/', views.update_org, name = "update_org"),


    path('orgs/', views.create_dataset, name = "create_dataset"),
    path('orgs/get/<int:dataset_id>/', views.get_dataset, name = "get_dataset"),
    path('orgs/delete/<int:dataset_id>/', views.delete_dataset, name = "delete_dataset"),
    path('orgs/update/<int:dataset_id>/', views.update_dataset, name = "update_dataset"),

]