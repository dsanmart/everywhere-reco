"""This module contains functions to download the datasets from drive."""


import pandas as pd


def get_users_data():
    """Downloads the users dataset and returns a pandas dataframe."""
    url = url_to_drive("https://drive.google.com/file/d/1DOz_YmB6VgLg3z6Xy9R6iYP6lVphK4o4/view?usp=share_link")
    return pd.read_csv(url)


def get_events_data():
    """Downloads the events dataset from drive and returns a pandas dataframe."""
    url = url_to_drive("https://drive.google.com/file/d/1KehUtKFzjqGOxHMFNO9tf-MR5QRR7H9J/view?usp=share_link")
    return pd.read_csv(url)


def get_train_data():
    """Downloads the train dataset from drive and returns a pandas dataframe."""
    url = url_to_drive("https://drive.google.com/file/d/1zAdnZ1oBMaGfQAlKdQhM47oYt2zEAGx8/view?usp=share_link")
    return pd.read_csv(url)


def get_user_friends_data():
    """Downloads the user_friends dataset from drive and returns a pandas dataframe."""
    url = url_to_drive("https://drive.google.com/file/d/1-U8ZBxhjtXYXG51Tiu6N-mNbOTh51UjE/view?usp=share_link")
    return pd.read_csv(url)


def get_event_attendees_data():
    """Downloads the event_attendees dataset from drive and returns a pandas dataframe."""
    url = url_to_drive("https://drive.google.com/file/d/1MrNT9GCUsyaIsCu3-wcThIMwgTTSp7EL/view?usp=share_link")
    return pd.read_csv(url)


def url_to_drive(url):
    """Converts a google drive url to a downloadable url."""
    url = 'https://www.googleapis.com/drive/v3/files/' + url.split('/')[-2] + '?alt=media&key=' + 'AIzaSyBdwGSwa_64SYxbOIgSkVflc3wz8ljU248'
    return url
