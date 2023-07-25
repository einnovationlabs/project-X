"""
DAO (Data Access Object) file

Helper file containing functions for accessing data in our database
"""
from user.models import Dataset

def create_dataset(dataset_data):

    dataset = dataset(firstname = dataset_data.get('firstname'), 
            lastname = dataset_data.get('lastname'), 
            datasetname = dataset_data.get('datasetname'),
            password = dataset_data.get('password'),
            about = dataset_data.get('about'),
            email = dataset_data.get('email'),
            phone_number = dataset_data.get('phone_number'),
            profile_pic = dataset_data.get('profile_pic')
            )
    
    
    dataset.save()

    return dataset



def update_dataset(dataset_id, dataset_data):

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