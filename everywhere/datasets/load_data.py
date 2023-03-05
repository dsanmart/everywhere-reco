"""This module contains functions to download the datasets from drive."""

import os
import pandas as pd


def maybe_download(filepath, url, dataset_name=None):
    """
    Downloads a dataset from a given Google Drive URL if it is not already downloaded, and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.
    url (str): The Google Drive URL of the dataset.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded dataset.
    """
    if not os.path.exists(filepath):
        print("Downloading", dataset_name, "dataset from external url:", url)
        url = url_to_drive(url)
        df = pd.read_csv(url)
        df.to_csv(filepath, index=False)
        return df
    else:
        print("Found", dataset_name, "in local 🎉")
        return pd.read_csv(filepath)


def get_users_data(filepath):
    """
    Downloads the users dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded users dataset.
    """
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1DOz_YmB6VgLg3z6Xy9R6iYP6lVphK4o4/view?usp=share_link", dataset_name="users")
    return df


def get_events_data(filepath):
    """
    Downloads the events dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded events dataset.
    """
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1KehUtKFzjqGOxHMFNO9tf-MR5QRR7H9J/view?usp=share_link", dataset_name="events")
    return df


def get_train_data(filepath):
    """
    Downloads the train dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded train dataset.
    """
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1zAdnZ1oBMaGfQAlKdQhM47oYt2zEAGx8/view?usp=share_link", dataset_name="train")
    return df


def get_user_friends_data(filepath):
    """
    Downloads the user_friends dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded user_friends dataset.
    """
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1-U8ZBxhjtXYXG51Tiu6N-mNbOTh51UjE/view?usp=share_link", dataset_name="user_friends")
    return df


def get_event_attendees_data(filepath):
    """
    Downloads the event_attendees dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded event_attendees dataset.
    """
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1MrNT9GCUsyaIsCu3-wcThIMwgTTSp7EL/view?usp=share_link", dataset_name="event_attendees")
    return df


def url_to_drive(url):
    """
    Converts a Google Drive URL to a downloadable URL that can be used to download files.

    Args:
    url (str): The Google Drive URL of a file.

    Returns:
    str: The downloadable URL of the file.

    Raises:
    ValueError: If the DRIVE_API environment variable is not set.
    """
    if os.getenv('DRIVE_API') is None:
        raise ValueError("DRIVE_API environment variable is not set")
    else:
        url = 'https://www.googleapis.com/drive/v3/files/' + url.split('/')[-2] + '?alt=media&key=' + os.getenv('DRIVE_API')
    return url
