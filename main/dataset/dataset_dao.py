"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from dataset.models import Dataset
from dataset.models import DatasetFile
from dataset.models import DatasetAddtFile
from dataset.models import DatasetTag
from dataset.models import DatasetMetadata

def create_dataset(dataset_data):
    """
    Creates dataset given dataset_data
    """
    dataset = Dataset(
            is_verified = dataset_data.get('is_verified'), 
            has_user_policy = dataset_data.get('has_user_policy'), 
            is_government = dataset_data.get('is_government'),
            is_public = dataset_data.get('is_public'),
            status = dataset_data.get('status'),
            addt_info = dataset_data.get('addt_info'),
            number_of_likes = dataset_data.get('number_of_likes'),
            profile_pic = dataset_data.get('profile_pic')
            )
    
    
    dataset.save()

    DatasetFile = DatasetFile(
            file_url = dataset_data.get("DatasetFiles").get("file_url")
    )
    DatasetFile.save()

    for dataset_title, url in dataset_data.get("DatasetFiles").get("addt_files"):
        DatasetAddtFile = DatasetAddtFile(title = dataset_title, file_url = url)
        DatasetAddtFile.save()

    for tag_name in dataset.get("tags"):
        tag = DatasetTag(name = tag_name)
        tag.save()

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

    return dataset


def update_dataset(dataset_id, dataset_data):
    """
    Updates and returns dataset given dataset_id and dataset_data
    """
    dataset = dataset.objects.get(id = dataset_id)

    dataset.firstname = dataset_data.get('firstname')
    dataset.lastname = dataset_data.get('lastname')
    dataset.datasetname = dataset_data.get('datasetname')
    dataset.password = dataset_data.get('password')
    dataset.about = dataset_data.get('about')
    dataset.email = dataset_data.get('email')
    dataset.phone_number = dataset_data.get('phone_number')
    dataset.profile_pic = dataset_data.get('profile_pic')

    dataset.save()

    return dataset


def delete_dataset(dataset_id):
    dataset = dataset.objects.get(id = dataset_id)
    dataset.is_active = False
    dataset.save()
    return dataset


def get_dataset(dataset_id):
    """
    Retrieves and Returns dataset given dataset_id
    """