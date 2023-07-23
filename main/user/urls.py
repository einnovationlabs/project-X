from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('getuser/<int:id>/', views.get_user, name='get_user'),
    path('createuser/', views.create_user, name='create_user'),
    path('deleteuser/<int:id>/', views.delete_user, name='delete_user'),
    path('updateuser/<int:id>/', views.update_user, name='update_user'),

]