from django.urls import path

from . import views

urlpatterns = [
    path("datasets.create", views.create_dataset, name="create_dataset"),
    path("datasets.list", views.get_all_datasets, name="get_all_datasets"),
    path("datasets.info/<int:dataset_id>", views.get_dataset, name="get_dataset"),
    path(
        "datasets.delete/<int:dataset_id>", views.delete_dataset, name="delete_dataset"
    ),
    path(
        "datasets.update/<int:dataset_id>", views.update_dataset, name="update_dataset"
    ),
    path("files.create/<int:user_id>", views.create_file, name="create_file"),
    path(
        "files.delete/<int:user_id>/<int:file_id>",
        views.delete_file,
        name="delete_file",
    ),
    path("comments.create/<int:user_id>", views.create_comment, name="create_comment"),
    path("comments.delete", views.delete_comment, name="delete_comment"),
    path("likes.create/<int:user_id>", views.create_like, name="create_like"),
    path("likes.delete/<int:user_id>", views.delete_like, name="delete_like"),
    path(
        "bookmarks.create/<int:user_id>/", views.create_bookmark, name="create_bookmark"
    ),
    path(
        "bookmarks.delete/<int:user_id>/", views.delete_bookmark, name="delete_bookmark"
    ),
]

# /datasets.create
# /datasets.update
# /datasets.delete
# /datasets.archive
# /datasets.info
# /datasets.list
# /datasets.download
# /datasets.approve
# /datasets.publish
# /datasets.unPublish
# /datasets.removeApproval
# /datasets.listForAdmin
# /datasets.listForSuperAdmin
