"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from apps.dataset.models import Dataset
from apps.dataset.models import File
from apps.dataset.models import Tag
from apps.dataset.models import Dataset_Metadata
from apps.user.crud import get_user
from apps.dataset.models import Comment
from apps.dataset.models import Like
from apps.dataset.models import Bookmark
from apps.organization.crud import get_org

from apps.users.errors import UserNotFound

def _create_dataset_files(files):
    dataset_files = []
    for dataset_title, url in files:
        file = File(title = dataset_title, file_url = url, owner_user = owner_user)
        file.save()
        dataset_files.append(file)

def _create_dataset_tags(tags):
    dataset_tags = []
    for tag_name in dataset_tags:
        tag = Tag(name = tag_name)
        tag.save()
        tags.append(tag)

def create_dataset(data, user_id):
    """
    Creates dataset given data
    """
    owner = get_user(user_id)
    if not owner:
        raise 

    metadata = Dataset_Metadata(
            metadata_file = data.get("metadata").get("metadata_file"),
            metadata_blurb = data.get("metadata").get("metadata_blurb"),
            metadata_source_link = data.get("metadata").get("metadata_source_link"),
            metadata_resource_type = data.get("metadata").get("metadata_resource_type"),
            publisher = data.get("metadata").get("publisher"),
            maintainer = data.get("metadata").get("maintainer"),
            license_link = data.get("metadata").get("license_link")
    )
    metadata.save()

    dataset = Dataset(
            is_verified = data.get('is_verified'), 
            has_user_policy = data.get('has_user_policy'), 
            is_government = data.get('is_government'),
            is_public = data.get('is_public'),
            title=data.get('title'),
            description=data.get('description'),
            status = data.get('status'),
            addt_info = data.get('addt_info'),
            owner_user = owner,
            dataset_metadata = metadata
            )
    
    dataset.files = _create_dataset_files(data.get("files"))
    dataset.tags = _create_dataset_tags(data.get("tags"))
        
    dataset.save()

    res = {
        "dataset" : dataset.serialize(),
        "dataset_tags" : tags,
        "dataset_files" : files
    }
    return res


def update_dataset(dataset_id, dataset_data):
    """
    Updates and returns dataset given dataset_id and dataset_data
    """
    dataset = Dataset.objects.get(id = dataset_id)

    metadata = dataset.dataset_metadata
    metadata.metadata_file = dataset_data.get("metadata").get("metadata_file")
    metadata.metadata_title = dataset_data.get("metadata").get("metadata_title")
    metadata.metadata_blurb = dataset_data.get("metadata").get("metadata_blurb")
    metadata.metadata_source_link = dataset_data.get("metadata").get("metadata_source_link")
    metadata.metadata_resource_type = dataset_data.get("metadata").get("metadata_resource_type")
    metadata.publisher = dataset_data.get("metadata").get("publisher")
    metadata.maintainer = dataset_data.get("metadata").get("maintainer")
    metadata.license_link = dataset_data.get("metadata").get("license_link")

    metadata.save()

    dataset.is_verified = dataset_data.get('is_verified')
    dataset.has_user_policy = dataset_data.get('has_user_policy')
    dataset.is_government = dataset_data.get('is_government')
    dataset.is_public = dataset_data.get('is_public')
    dataset.status = dataset_data.get('status')
    dataset.addt_info = dataset_data.get('addt_info')
    dataset.number_of_likes = dataset_data.get('number_of_likes')
    dataset.csv_file_url = dataset_data.get("csv_file_url")

    dataset.save()

    return dataset


def delete_dataset(dataset_id):
    dataset = Dataset.objects.get(id = dataset_id)
    dataset.is_deleted = True
    dataset.save()
    dataset = Dataset.objects.get(id = dataset_id)
    return dataset


def get_dataset(dataset_id):
    """
    Retrieves and Returns dataset given dataset_id
    """
    return {"dataset": Dataset.objects.get(id = dataset_id)}

def get_all_datasets():
    """
    Retrieves and Returns all datasets
    """
    return {"datasets" : [dataset.serialize() for dataset in Dataset.objects.filter(is_deleted=False).all()]}


def create_tag():
    """
    """
    tag = Tag(name = tag_name, dataset = dataset)


def delete_tag(tag_id):
    """
    """

def create_file(user_id, file_data):
    """
    Creates and Returns file by user
    """
    owner = get_user(user_id)
    file = File(title = file_data.get("title"), file_url = file_data.get("url"), owner_user = owner)
    file.save()
    return file.serialize()


def delete_file(user_id, file_id):
    """
    Deletes and Returns file by user
    """
    file = File.objects.filter(id = file_id).first()
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
    comment = Comment(dataset = dataset, owner_user = owner, body = comment_data.get("body"))
    comment.save()

    return comment.serialize()

def delete_comment(user_id, comment_id):
    """
    Deletes and Returns comment by user
    """
    comment = Comment.objects.filter(id = comment_id).first()
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
    like = Like.objects.filter(owner_user = user, dataset = dataset, status = True).first()

    if like:
        return False, like
    
    like = Like(user = user, dataset = dataset)
    like.save()
    return like

def delete_like(user_id, like_id):
    """
    Deletes and Returns like by user
    """

    like = Like.objects.filter(id = like_id).first()
    if like_id.owner_user.id != user_id:
        return False, like
    like.status = False
    like.save()

    return True, like.serialize()

def create_bookmark(user_id, bookmark_data):
    """
    Creates and Returns bookmark by user
    """
    dataset = dataset = get_dataset(bookmark_data.get("dataset_id"))
    user = get_user(user_id)
    bookmark = Bookmark.objects.filter(owner_user = user, dataset = dataset, status = True).first()

    if bookmark:
        return False, bookmark
    
    bookmark = Bookmark(user = user, dataset = dataset)
    bookmark.save()
    return bookmark

def delete_bookmark(user_id, bookmark_id):
    """
    Deletes and Returns bookmark by user
    """

    bookmark = Bookmark.objects.filter(id = bookmark_id).first()
    if bookmark_id.owner_user.id != user_id:
        return False, bookmark
    bookmark.status = False
    bookmark.save()

    return True, bookmark.serialize()

def add_owner_org(user_id, dataset_data):
    """
    Adds owner org to dataset by user
    """
    dataset = get_dataset(dataset_data.get("dataset_id"))
    org = get_org(dataset_data.gete("org_id"))

    if dataset.owner_user.id != user_id:
        return False, dataset
    dataset.owner_org = org
    dataset.save()

    return True, dataset  #TODO: remove owner org or just update


def publish_dataset(user_id, dataset_id):
    """
    Publishes dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_published = True
    dataset.save()

    return True, dataset


def unpusblish_dataset(user_id, dataset_id):
    """
    Unpublishes dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_published = False
    dataset.save()

    return True, dataset

def archive_dataset(user_id, dataset_id):
    """
    Archives dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_archived = True
    dataset.save()

    return True, dataset

def unarchive_dataset(user_id, dataset_id):
    """
    Unarchives dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_archived = False
    dataset.save()

    return True, dataset

def approve_dataset(user_id, dataset_id):
    """
    Approves dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_approved = True
    dataset.save()

    return True, dataset

def disapprove_dataset(user_id, dataset_id):
    """
    Disapproves dataset by user
    """
    dataset = get_dataset(dataset_id)
    if dataset.owner_user.id != user_id:
        return False, dataset
    
    dataset.is_approved = False
    dataset.save()

    return True, dataset

# TODO: if depends on condition, use tuple returns else return serialized()