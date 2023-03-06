import pandas as pd
import pytest
from  everywhere.datasets.load_data import get_users_data, get_train_data, get_user_friends_data, get_event_attendees_data
from dotenv import load_dotenv


load_dotenv() # load environment variables

def test_get_users_data():
    """Test the 'get_users_data' function to ensure it downloads the expected columns.
    
    Returns:
        None
    """
    df = get_users_data(force_download=True)
    for col_name in ['user_id', 'locale', 'birthyear', 'gender', 'joinedAt', 'location', 'timezone']:
        assert col_name in df.columns

def test_get_train_data():
    """Test the 'get_train_data' function to ensure it downloads the expected columns.
    
    Returns:
        None
    """
    df = get_train_data(force_download=True)
    for col_name in ['user', 'event', 'invited', 'timestamp', 'interested', 'not_interested']:
        assert col_name in df.columns

def test_get_event_attendees_data():
    """Test the 'get_event_attendees_data' function to ensure it downloads the expected columns.
    
    Returns:
        None
    """
    df = get_event_attendees_data(force_download=True)
    for col_name in ['event', 'yes', 'maybe', 'invited', 'no']:
        assert col_name in df.columns

def test_get_user_friends_data():
    """Test the 'get_user_friends_data' function to ensure it downloads the expected columns.
    
    Returns:
        None
    """
    df = get_user_friends_data(force_download=True)
    for col_name in ['user', 'friends']:
        assert col_name in df.columns



# Not testing events data because it take too long to download
