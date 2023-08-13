"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from dataset.models import Dataset
from dataset.models import File
from dataset.models import Tag
from dataset.models import DatasetMetadata
from user.user_dao import get_user
from dataset.models import Comment
from dataset.models import Like
from dataset.models import Bookmark

def create_dataset(dataset_data, user_id):
    """
    Creates dataset given dataset_data
    """
    metadata = DatasetMetadata(
            metadata_file = dataset_data.get("metadata").get("metadata_file"),
            metadata_title = dataset_data.get("metadata").get("metadata_title"),
            metadata_blurb = dataset_data.get("metadata").get("metadata_blurb"),
            metadata_source_link = dataset_data.get("metadata").get("metadata_source_link"),
            metadata_resource_type = dataset_data.get("metadata").get("metadata_resource_type"),
            publisher = dataset_data.get("metadata").get("publisher"),
            maintainer = dataset_data.get("metadata").get("maintainer"),
            license_link = dataset_data.get("metadata").get("license_link")
    )
    metadata.save()

    owner_user = get_user(user_id)
    dataset = Dataset(
            is_verified = dataset_data.get('is_verified'), 
            has_user_policy = dataset_data.get('has_user_policy'), 
            is_government = dataset_data.get('is_government'),
            is_public = dataset_data.get('is_public'),
            status = dataset_data.get('status'),
            addt_info = dataset_data.get('addt_info'),
            owner_user = owner_user,
            dataset_metadata = metadata

            )
    
    dataset.save()
    files = []
    for dataset_title, url in dataset_data.get("dataset_files"):
        file = File(title = dataset_title, file_url = url, dataset = dataset, owner_user = owner_user)
        file.save()
        files.append(file.serialize())

    tags = []
    for tag_name in dataset_data.get("tags"):
        tag = Tag(name = tag_name, dataset = dataset)
        tag.save()
        tags.append(tag.serialize())
        
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

    return dataset


def get_dataset(dataset_id):
    """
    Retrieves and Returns dataset given dataset_id
    """
    dataset = Dataset.objects.get(id = dataset_id)
    files =  []
    for file in File.objects.filter(dataset = dataset).all():
        files.append(file.serialize())
    tags = []
    for tag in Tag.objects.filter(dataset = dataset).all():
        tags.append(tag.serialize())

    
    comments = []
    for comment in Comment.objects.filter(dataset = dataset).all():
        comments.append(comment.serialize())

    likes = []
    for like in Like.objects.filter(dataset = dataset).all():
        likes.append(like.serialize())
    res = {
        "dataset" : dataset.serialize(),
        "dataset_comments" : comments,
        "dataset_tags" : tags,
        "dataset_files" : files,
        "dataset_likes" : likes,
    }
    return res

def get_all_datasets():
    """
    Retrieves and Returns all datasets
    """
    datasets = Dataset.objects.all()
    res = []

    for dataset in datasets:
        res.append(dataset.serialize())

    return {"datasets" : res}


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

# TODO: if depends on condition, use tuple returns else return serialized()