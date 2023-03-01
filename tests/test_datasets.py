import pandas as pd
import pytest
from  everywhere.datasets.load_data import get_users_data
from everywhere.utils.constants import DEFAULT_USER_DF, DEFAULT_TRAIN_DF, DEFAULT_FRIENDS_DF


def url_to_drive(url):
    """Converts a google drive url to a downloadable url."""
    url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
    return url


def test_get_user_data():
    """Downloads the users dataset and returns the url."""
    df=pd.read_csv( url_to_drive("https://drive.google.com/file/d/1DOz_YmB6VgLg3z6Xy9R6iYP6lVphK4o4/view?usp=share_link"))
    for col_name in DEFAULT_USER_DF:
        assert col_name in df.columns



def test_get_train_data():
    """Downloads the train dataset from drive and returns the url."""
    df =pd.read_csv( url_to_drive("https://drive.google.com/file/d/1zAdnZ1oBMaGfQAlKdQhM47oYt2zEAGx8/view?usp=share_link"))
    for col_name in DEFAULT_TRAIN_DF:
        assert col_name in df.columns


'''
def test_get_events_data():
    """Downloads the events dataset from drive and returns the url."""
    df = pd-read_csv(url_to_drive("https://drive.google.com/file/d/1KehUtKFzjqGOxHMFNO9tf-MR5QRR7H9J/view?usp=share_link"))
        assert len(df.columns) == 102
'''


'''

def test_get_user_friends_data():
    """Downloads the user_friends dataset from drive and returns the url."""
    df = pd.read_csv( url_to_drive("https://drive.google.com/file/d/1-U8ZBxhjtXYXG51Tiu6N-mNbOTh51UjE/view?usp=share_link"))
    for col_name in DEFAULT_FRIENDS_DF:
        assert col_name in df.columns
'''




