"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from dataset.models import Dataset
from dataset.models import File
from dataset.models import Tag
from dataset.models import Metadata
from user.user_dao import get_user
from dataset.models import Comment
from dataset.models import Like
from dataset.models import Bookmark
from organization.organization_dao import get_org
def create_dataset(dataset_data, user_id):
    """
    Creates dataset given dataset_data
    """
    exists, owner_user = get_user(user_id)

    if not exists:
        return False, None

    metadata = Metadata(
            file = dataset_data.get("metadata").get("file"),
            title = dataset_data.get("metadata").get("title"),
            blurb = dataset_data.get("metadata").get("blurb"),
            source_link = dataset_data.get("metadata").get("source_link"),
            resource_type = dataset_data.get("metadata").get("resource_type"),
            publisher = dataset_data.get("metadata").get("publisher"),
            maintainer = dataset_data.get("metadata").get("maintainer"),
            license_link = dataset_data.get("metadata").get("license_link")
    )
    metadata.save()

    dataset = Dataset(
            is_verified = dataset_data.get('is_verified'), 
            has_user_policy = dataset_data.get('has_user_policy'), 
            is_government = dataset_data.get('is_government'),
            is_public = dataset_data.get('is_public'),
            addt_info = dataset_data.get('addt_info'),
            owner_user = owner_user,
            metadata = metadata

            )
    
    dataset.save()
    for title, url in dataset_data.get("files"):
        try:
            file = File.objects.get(url = url)
        except:
            file = File(title = title, url = url) 
        file.save()
        dataset.files.add(file)

    for tag_name in dataset_data.get("tags"):
        try:
            tag = Tag.objects.get(name = tag_name)
        except:
            tag = Tag(name = tag_name) 
        tag.save()
        dataset.tags.add(tag)
        
    dataset.save()

    return True, dataset


def update_dataset(dataset_id, dataset_data):
    """
    Updates and returns dataset given dataset_id and dataset_data
    """
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None

    metadata = dataset.dataset_metadata

    metadata.file = dataset_data.get("metadata").get("file")
    metadata.title = dataset_data.get("metadata").get("title")
    metadata.blurb = dataset_data.get("metadata").get("blurb")
    metadata.source_link = dataset_data.get("metadata").get("source_link")
    metadata.resource_type = dataset_data.get("metadata").get("resource_type")
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

    return True, dataset


def delete_dataset(dataset_id):
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None
    
    dataset.is_deleted = True
    dataset.save()

    return True, dataset


def get_dataset(dataset_id):
    """
    Retrieves and Returns serialized dataset given dataset_id
    """
    dataset = Dataset.objects.get(id = dataset_id)

    if not dataset:
        return False, None
    
    return True, dataset
    

def get_all_datasets():
    """
    Retrieves and Returns all datasets
    """
    datasets = Dataset.objects.all()
    res = []

    for dataset in datasets:
        res.append(dataset.serialize())

    return True, {"datasets" : res}

#TODO: tag
def create_tag(dataset_id, tag_data):
    """
    Creates and Returns Tag given dataset_id
    """
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None
    tag_name = tag_data.get("name")
    try:
        tag = Tag.objects.get(name = tag_name)
    except:
        tag = Tag(name = tag_name)
    tag.save()
    dataset.tags.add(tag)
    dataset.save()

    return True, tag

def get_tag(tag_id):
    """
    Retrieves and Returns Tag given tag_id
    """
    tag = Tag.objects.get(id = tag_id)

    if not tag:
        return False, tag

    return True, tag


def delete_tag(tag_id, dataset_id):
    """
    Deletes and Returns Tag given dataset_id
    """
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None
    
    success, tag = get_tag(tag_id)

    if not success:
        return False, None
    dataset.tags.remove(tag)

    dataset.save()

    return True, tag

# TODO : file
def create_file(dataset_id, file_data):
    """
    Creates and Returns file given dataset_id
    """
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None
    
    file = File(title = file_data.get("title"), url = file_data.get("url"))
    file.save()

    dataset.files.add(file)

    dataset.save()

    return True, file


def delete_file(dataset_id, file_id):
    """
    Deletes and Returns file given dataset_id
    """
    success, dataset = get_dataset(dataset_id)

    if not success:
        return False, None
    
    success, file = get_file(file_id)

    if not success:
        return False, None
    dataset.files.remove(file)

    dataset.save()

    return True, file

def get_file(file_id):
    """
    Retrieves and Returns file given file_id
    """
    file = file.objects.get(id = file_id)

    if not file:
        return False, file

    return True, file

# TODO: COMMENT
def create_comment(user_id, comment_data):
    """
    Creates and Returns comment by user
    """
    success, dataset = get_dataset(comment_data.get("dataset_id"))

    if not success:
        return False, None
    success, user = get_user(user_id)

    if not success:
        return False, None
    
    comment = Comment(user = user, dataset = dataset, body = comment_data.get("body"))

    comment.save()

    return comment

def delete_comment(user_id, comment_id):
    """
    Deletes and Returns comment by user
    """
    success, comment = get_comment(id = comment_id)
    if not success or (success and comment.user.id != user_id):
        return False, None
    
    comment.status = False
    comment.save()
    return True, comment

def get_comment(comment_id):
    """
    Retrieves and Returns comment given comment_id
    """
    comment = Comment.objects.get(id = comment_id)

    if not comment:
        return False, comment

    return True, comment

#TODO: like
def create_like(user_id, like_data):
    """
    Creates and Returns like by user
    """
    success, dataset = get_dataset(like_data.get("dataset_id"))

    if not success:
        return False, None
    success, user = get_user(user_id)

    if not success:
        return False, None
    
    like = Like(user = user, dataset = dataset)

    like.save()

    return like


def delete_like(user_id, like_id):
    """
    Deletes and Returns like by user
    """
    success, like = get_like(id = like_id)
    if not success or (success and like.user.id != user_id):
        return False, None
    
    like.status = False
    like.save()
    return True, like


def get_like(like_id):
    """
    Retrieves and Returns like given like_id
    """
    like = like.objects.get(id = like_id)

    if not like:
        return False, like

    return True, like


# TODO: bookmark
def create_bookmark(user_id, bookmark_data):
    """
    Creates and Returns bookmark by user
    """
    success, dataset = get_dataset(bookmark_data.get("dataset_id"))

    if not success:
        return False, None
    success, user = get_user(user_id)

    if not success:
        return False, None
    
    bookmark = Bookmark(user = user, dataset = dataset)

    bookmark.save()

    return bookmark

def delete_bookmark(user_id, bookmark_id):
    """
    Deletes and Returns bookmark by user
    """
    success, bookmark = get_bookmark(id = bookmark_id)
    if not success or (success and bookmark.user.id != user_id):
        return False, None
    
    bookmark.status = False
    bookmark.save()
    return True, bookmark

def get_bookmark(bookmark_id):
    """
    Retrieves and Returns bookmark given bookmark_id
    """
    bookmark = Bookmark.objects.get(id = bookmark_id)

    if not bookmark:
        return False, bookmark

    return True, bookmark

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


