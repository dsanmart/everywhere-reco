"""Helper functions for loading/downloading data."""

import os
import pandas as pd


def maybe_download(filepath, url, dataset_name=None, force_download=False):
    """
    Downloads a dataset from a given Google Drive URL if it is not already downloaded, and returns a pandas dataframe containing the dataset.

    Args:
    filepath (str): The path to the local file where the dataset should be saved or is already saved.
    url (str): The Google Drive URL of the dataset.

    Returns:
    pandas.DataFrame: A dataframe containing the downloaded dataset.
    """
    if not os.path.exists(filepath) or force_download==True:
        print("Downloading", dataset_name, "dataset from external url:", url)
        url = url_to_drive(url)
        df = pd.read_csv(url)
        df.to_csv(filepath, index=False)
        return df
    else:
        print("Found", dataset_name, "in local 🎉")
        return pd.read_csv(filepath)
    

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