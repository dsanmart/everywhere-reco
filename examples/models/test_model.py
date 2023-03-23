# Databricks notebook source
# MAGIC %md
# MAGIC #### Everywhere preprocessing

# COMMAND ----------
import os 
import pandas as pd
import numpy as np
from dotenv import load_dotenv  # load environment variables
from imblearn.under_sampling import ClusterCentroids
from collections import Counter
from everywhere.datasets.load_data import (
    get_users_data,
    get_events_data,
    get_train_data,
    get_user_friends_data,
    get_event_attendees_data,
)

from everywhere.datasets.feature_extractor import (
    get_friends_attendee_nums,
    get_event_attendee_nums,
)

# COMMAND ----------


# MAGIC %md #### Load Datasets

# COMMAND ----------
# load environment variables
load_dotenv()  


# COMMAND ----------

# MAGIC %md #### Load Users Data

# COMMAND ----------

df_users = get_users_data(cloud=True)
print(df_users.shape)
df_users.head()

# COMMAND ----------

# MAGIC %md #### Load user Friends Data

# COMMAND ----------

df_user_friends = get_user_friends_data(cloud=True)
print(df_user_friends.shape)
df_user_friends.head()

# COMMAND ----------

# MAGIC %md #### Load Events Attendees Data

# COMMAND ----------
df_event_attendees = get_event_attendees_data(cloud=True)
print(df_event_attendees.shape)
df_event_attendees.head()

# COMMAND ----------


# MAGIC %md #### Load train Data

# COMMAND ----------
df_train = get_train_data(cloud=True)
print(df_train.shape)
df_train.head()

# COMMAND ----------


# MAGIC %md #### Load Events Data

# COMMAND ----------
df_events = get_events_data(cloud=True)
print(df_events.shape)
df_events.head()

# COMMAND ----------

# MAGIC %md #### Feature Engineering

# COMMAND ----------
df_train = get_friends_attendee_nums(df_train, df_user_friends, df_event_attendees)
df_train

# COMMAND ----------

# MAGIC %md #### Merge with Events Data

# COMMAND ----------
df_train = get_event_attendee_nums(df_train, df_event_attendees)
print(df_train.shape)
df_train.head()

# COMMAND ----------

# MAGIC %md #### Merge with Users Data

# COMMAND ----------

df_events_clean = df_events.drop(
    columns=["user_id", "start_time", "city", "state", "zip", "country", "lat", "lng"]
)
# Merge with events
df_train = pd.merge(
    df_train, df_events_clean, how="inner", left_on="event", right_on="event_id"
)
df_train = df_train.drop(columns=["invited_y", "timestamp", "yes", "maybe", "no"])
df_train

# COMMAND ----------


# MAGIC %md #### Balance dataset with Cluster Centroid

# COMMAND ----------
data = df_train.copy()
X = data.drop("interested", axis=1)
y = data["interested"]
print("Original dataset shape {}".format(Counter(y)))
cc = ClusterCentroids(random_state=42)
X_res, y_res = cc.fit_resample(X, y)
print("Resampled dataset shape {}".format(Counter(y_res)))

# COMMAND ----------

# MAGIC %md #### Shuffle Data

# COMMAND ----------

final = pd.merge(X_res, y_res, left_index=True, right_index=True)
final = final.iloc[np.random.permutation(final.index)].reset_index(drop=True)
final

# COMMAND ----------







