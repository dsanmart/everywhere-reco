"""This module contains functions to download the datasets from drive."""

import os
import pandas as pd
from everywhere.utils.data import maybe_download


def get_users_data(filepath="local_data/users.csv", force_download=False):
    """
    Downloads the users dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded users dataset.
    """

    # if local_data doesnt exists, create it
    if not os.path.exists("local_data"):
        os.mkdir("local_data")


    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1DOz_YmB6VgLg3z6Xy9R6iYP6lVphK4o4/view?usp=share_link", dataset_name="users", force_download=force_download)
    return df


def get_events_data(filepath="local_data/events.csv", force_download=False):
    """
    Downloads the events dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded events dataset.
    """

    # if local_data doesnt exists, create it
    if not os.path.exists("local_data"):
        os.mkdir("local_data")
        
    df = maybe_download(filepath=filepath, url="https://drive.google.com/file/d/1KehUtKFzjqGOxHMFNO9tf-MR5QRR7H9J/view?usp=share_link", 
                        dataset_name="events", 
                        force_download=force_download)
    return df


def get_train_data(filepath="local_data/train.csv", force_download=False):
    """
    Downloads the train dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded train dataset.
    """

    # if local_data doesnt existscreate it

    if not os.path.exists("local_data"):
        os.mkdir("local_data")
        
    df = maybe_download(filepath=filepath, 
                        url="https://drive.google.com/file/d/1zAdnZ1oBMaGfQAlKdQhM47oYt2zEAGx8/view?usp=share_link", 
                        dataset_name="train", 
                        force_download=force_download)
    return df


def get_user_friends_data(filepath="local_data/user_friends.csv", force_download=False):
    """
    Downloads the user_friends dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded user_friends dataset.
    """

    # if local_data doesnt exists, create it
    if not os.path.exists("local_data"):
        os.mkdir("local_data")
        
    df = maybe_download(filepath=filepath, 
                        url="https://drive.google.com/file/d/1-U8ZBxhjtXYXG51Tiu6N-mNbOTh51UjE/view?usp=share_link", 
                        dataset_name="user_friends",
                        force_download=force_download)
    return df


def get_event_attendees_data(filepath="local_data/event_attendees.csv", force_download=False):
    """
    Downloads the event_attendees dataset from Google Drive and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded event_attendees dataset.
    """
    df = maybe_download(filepath=filepath, 
                        url="https://drive.google.com/file/d/1MrNT9GCUsyaIsCu3-wcThIMwgTTSp7EL/view?usp=share_link", 
                        dataset_name="event_attendees",
                        force_download=force_download)
    return df
