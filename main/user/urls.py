from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),

    path('users/get/<int:user_id>/', views.get_user, name='get_user'),
    path('users/', views.create_user, name='create_user'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('users/update/<int:user_id>/', views.update_user, name='update_user'),
]