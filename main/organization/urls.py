from django.urls import path
from . import views

urlpatterns = [
    path('orgs/<int:admin_id>/', views.create_org, name = "create_org"),
    path('orgs/get/<int:org_id>/', views.get_org, name = "get_org"),
    path('orgs/delete/<int:org_id>/', views.delete_org, name = "delete_org"),
    path('orgs/update/<int:org_id>/', views.update_org, name = "update_org"),

]