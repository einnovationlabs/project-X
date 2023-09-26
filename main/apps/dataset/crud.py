""" CRUD for datasets. """
from apps.dataset.models import (Bookmark, Comment, Dataset, Dataset_Metadata,
                                 File, Like, Tag)
from apps.organization.crud import get_org
from apps.user.crud import get_user
from apps.user.models import User
from utils import error_response


def _create_dataset_files(dataset_id, files):
    res = []
    for title, url in files:
        file = File(title=title, file_url=url)
        file.save()
        res.append(file)

    return res


def _create_dataset_tags(dataset_id, tags):
    if not tags:
        return []

    res = []
    for name in tags:
        tag = Tag(name=name)
        tag.save()
        res.append(tag)

    return res


def create_dataset(data, user_id):
    """
    Creates dataset using `data` and sets user with id `user_id` as the author.
    """
    try:
        owner = get_user(user_id)

        dataset = Dataset()
        for field in Dataset.single_fields:
            setattr(dataset, field, data.get(field))

        dataset.owner_user = owner
        metadata = Dataset_Metadata(**data.get("metadata"))
        metadata.save()
        dataset.metadata = metadata
        dataset.save()

        if data.get("files"):
            _create_dataset_files(dataset.id, data.get("files"))
        if data.get("tags"):
            _create_dataset_tags(dataset.id, data.get("tags"))

        return {"dataset": dataset.serialize()}
    except User.DoesNotExist:
        return error_response("User does not exist!")


def update_dataset_metadata(metadata, data):
    metadata.file = data.get("metadata").get("file")
    metadata.metadata_title = data.get("metadata").get("metadata_title")
    metadata.metadata_blurb = data.get("metadata").get("metadata_blurb")
    metadata.metadata_source_link = data.get("metadata").get("metadata_source_link")
    metadata.metadata_resource_type = data.get("metadata").get("metadata_resource_type")
    metadata.publisher = data.get("metadata").get("publisher")
    metadata.maintainer = data.get("metadata").get("maintainer")
    metadata.license_link = data.get("metadata").get("license_link")

    metadata.save()


def update_dataset(dataset_id, data):
    dataset = Dataset.objects.get(id=dataset_id)
    if not dataset:
        return None

    for field in Dataset.single_fields:
        setattr(dataset, field, data.get(field))

    dataset.save()
    return {"dataset": dataset}


def delete_dataset(dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    dataset.is_deleted = True
    dataset.save()
    dataset = Dataset.objects.get(id=dataset_id)
    return {"dataset": dataset}


def get_dataset(dataset_id):
    """
    Retrieves and Returns dataset given dataset_id
    """
    return {"dataset": Dataset.objects.get(id=dataset_id)}


def get_all_datasets():
    """
    Retrieves and Returns all datasets
    """
    return {
        "datasets": [
            dataset.serialize()
            for dataset in Dataset.objects.filter(is_deleted=False).all()
        ]
    }


def delete_tag(tag_id):
    """ """


def create_file(user_id, file_data):
    """
    Creates and Returns file by user
    """
    owner = get_user(user_id)
    file = File(
        title=file_data.get("title"), file_url=file_data.get("url"), owner_user=owner
    )
    file.save()
    return file.serialize()


def delete_file(user_id, file_id):
    file = File.objects.filter(id=file_id).first()
    if file.owner_user.id != user_id:
        return file.serialize()
    file.status = False
    file.save()
    return file.serialize()


def create_comment(user_id, comment_data):
    """
    Creates and Returns comment by user
    """
    owner = get_user(user_id)
    dataset = get_dataset(comment_data.get("dataset_id"))
    comment = Comment(dataset=dataset, owner_user=owner, body=comment_data.get("body"))
    comment.save()

    return comment.serialize()


def delete_comment(user_id, comment_id):
    """
    Deletes and Returns comment by user
    """
    comment = Comment.objects.filter(id=comment_id).first()
    if comment.owner_user.id != user_id:
        return comment.serialize()
    comment.status = False
    comment.save()
    return comment.serialize()


def create_like(user_id, like_data):
    """
    Creates and Returns like by user
    """
    dataset = dataset = get_dataset(like_data.get("dataset_id"))
    user = get_user(user_id)
    like = Like.objects.filter(owner_user=user, dataset=dataset, status=True).first()

    if like:
        return like

    like = Like(user=user, dataset=dataset)
    like.save()
    return like


def delete_like(user_id, like_id):
    """
    Deletes and Returns like by user
    """

    like = Like.objects.filter(id=like_id).first()
    if like_id.owner_user.id != user_id:
        return like
    like.status = False
    like.save()

    return like.serialize()


def create_bookmark(user_id, bookmark_data):
    """
    Creates and Returns bookmark by user
    """
    dataset = dataset = get_dataset(bookmark_data.get("dataset_id"))
    user = get_user(user_id)
    bookmark = Bookmark.objects.filter(
        owner_user=user, dataset=dataset, status=True
    ).first()

    if bookmark:
        return bookmark

    bookmark = Bookmark(user=user, dataset=dataset)
    bookmark.save()
    return bookmark


def delete_bookmark(user_id, bookmark_id):
    """
    Deletes and Returns bookmark by user
    """

    bookmark = Bookmark.objects.filter(id=bookmark_id).first()
    if bookmark_id.owner_user.id != user_id:
        return bookmark
    bookmark.status = False
    bookmark.save()

    return bookmark.serialize()


def add_owner_org(user_id, dataset_data):
    """
    Adds owner org to dataset by user
    """
    dataset = get_dataset(dataset_data.get("dataset_id"))
    org = get_org(dataset_data.gete("org_id"))

    if dataset.owner_user.id != user_id:
        return dataset
    dataset.owner_org = org
    dataset.save()

    return dataset  # TODO: remove owner org or just update


def publish_dataset(user_id, dataset_id):
    """
    Publishes dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_published = True
    dataset.save()

    return dataset


def unpusblish_dataset(user_id, dataset_id):
    """
    Unpublishes dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_published = False
    dataset.save()

    return dataset


def archive_dataset(user_id, dataset_id):
    """
    Archives dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_archived = True
    dataset.save()

    return dataset


def unarchive_dataset(user_id, dataset_id):
    """
    Unarchives dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_archived = False
    dataset.save()

    return dataset


def approve_dataset(user_id, dataset_id):
    """
    Approves dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_approved = True
    dataset.save()

    return dataset


def disapprove_dataset(user_id, dataset_id):
    """
    Disapproves dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return dataset

    dataset.is_approved = False
    dataset.save()

    return dataset


# TODO: if depends on condition, use tuple returns else return serialized()
