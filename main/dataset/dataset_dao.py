"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from dataset.models import Dataset
from dataset.models import DatasetAddtFile
from dataset.models import DatasetTag
from dataset.models import DatasetMetadata
from user.user_dao import get_user

def create_dataset(dataset_data, owner_user_id):
    """
    Creates dataset given dataset_data
    """
    dataset_metadata = DatasetMetadata(
            metadata_file = dataset_data.get("metadata").get("metadata_file"),
            metadata_title = dataset_data.get("metadata").get("metadata_title"),
            metadata_blurb = dataset_data.get("metadata").get("metadata_blurb"),
            metadata_source_link = dataset_data.get("metadata").get("metadata_source_link"),
            metadata_resource_type = dataset_data.get("metadata").get("metadata_resource_type"),
            publisher = dataset_data.get("metadata").get("publisher"),
            maintainer = dataset_data.get("metadata").get("maintainer"),
            license_link = dataset_data.get("metadata").get("license_link")
    )
    dataset_metadata.save()

    owner_user = get_user(owner_user_id)
    dataset = Dataset(
            is_verified = dataset_data.get('is_verified'), 
            has_user_policy = dataset_data.get('has_user_policy'), 
            is_government = dataset_data.get('is_government'),
            is_public = dataset_data.get('is_public'),
            status = dataset_data.get('status'),
            addt_info = dataset_data.get('addt_info'),
            number_of_likes = dataset_data.get('number_of_likes'),
            csv_file_url = dataset_data.get("csv_file_url"),
            owner_user = owner_user,
            dataset_metadata = dataset_metadata
            )
    
    dataset.save()

    for dataset_title, url in dataset_data.get("dataset_files"):
        addt_file = DatasetAddtFile(title = dataset_title, file_url = url, file_dataset = dataset)
        addt_file.save()

    for tag_name in dataset_data.get("tags"):
        tag = DatasetTag(name = tag_name)
        tag.save()
        dataset.tags.add(tag)

    return dataset


def update_dataset(dataset_id, dataset_data):
    """
    Updates and returns dataset given dataset_id and dataset_data
    """
    dataset = Dataset.objects.get(id = dataset_id)

    dataset_metadata = dataset.metadata

    dataset_metadata.metadata_file = dataset_data.get("metadata").get("metadata_file")
    dataset_metadata.metadata_title = dataset_data.get("metadata").get("metadata_title")
    dataset_metadata.metadata_blurb = dataset_data.get("metadata").get("metadata_blurb")
    dataset_metadata.metadata_source_link = dataset_data.get("metadata").get("metadata_source_link")
    dataset_metadata.metadata_resource_type = dataset_data.get("metadata").get("metadata_resource_type")
    dataset_metadata.publisher = dataset_data.get("metadata").get("publisher")
    dataset_metadata.maintainer = dataset_data.get("metadata").get("maintainer")
    dataset_metadata.license_link = dataset_data.get("metadata").get("license_link")

    dataset_metadata.save()


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
    return dataset


def add_tag(tag_id):
    """
    """

def remove_tag(tag_id):
    """
    """

def add_file(file_id):
    """
    """

def remove_file(file_id):
    """
    """