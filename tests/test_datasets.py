import pandas as pd
import pytest
from  everywhere.datasets.load_data import get_users_data, get_train_data, get_user_friends_data, get_event_attendees_data
from dotenv import load_dotenv


load_dotenv() # load environment variables

def test_get_user_data():
    df = get_users_data(force_download=True)
    for col_name in ['user_id', 'locale', 'birthyear', 'gender', 'joinedAt', 'location',
       'timezone']:
        assert col_name in df.columns


def test_get_train_data():
    df = get_train_data(force_download=True)
    for col_name in ['user', 'event', 'invited', 'timestamp', 'interested',
       'not_interested']:
        assert col_name in df.columns


def test_get_event_attendees_data():
    df = get_event_attendees_data(force_download=True)
    for col_name in ['event', 'yes', 'maybe', 'invited', 'no']:
        assert col_name in df.columns


def test_get_user_friends_data():
    df = get_user_friends_data(force_download=True)
    for col_name in ['user', 'friends']:
        assert col_name in df.columns


# Not testing events data because it take too long to download
