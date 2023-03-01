'''This module contains functions extract features from the datasets.'''

import pandas as pd

def get_friends_status(row, event_attendees_df):
    """Returns the number of friends attending, not attending, maybe attending, and invited to the event."""

    event = row['event']
    friends = str(row['friends']).split(' ')
    ppl_attending = str(event_attendees_df.iloc[np.where(event_attendees_df['event']==event)[0][0]]['yes']).split(' ')
    ppl_not_attending = str(event_attendees_df.iloc[np.where(event_attendees_df['event']==event)[0][0]]['no']).split(' ')
    ppl_maybe_attending = str(event_attendees_df.iloc[np.where(event_attendees_df['event']==event)[0][0]]['maybe']).split(' ')
    ppl_invited = str(event_attendees_df.iloc[np.where(event_attendees_df['event']==event)[0][0]]['invited']).split(' ')
    friends_attending = list(set(friends).intersection(set(ppl_attending)))
    friends_not_attending = list(set(friends).intersection(set(ppl_not_attending)))
    friends_maybe_attending = list(set(friends).intersection(set(ppl_maybe_attending)))
    friends_invited = list(set(friends).intersection(set(ppl_invited)))
    
    return [len(friends_attending), len(friends_not_attending), len(friends_maybe_attending), len(friends_invited)]

def count_words(row, col_name):
    if(type(row[col_name]) != str):
        return 0
    return len(row[col_name].split())

def get_friends_attendee_nums(train_df, friends_df, event_attendees_df):
    # merge train_df with friends_df
    merged_df = pd.merge(train_df, friends_df, how='inner', left_on='user', right_on='user')
    merged_df['friends_attending'], merged_df['friends_not_attending'], merged_df['friends_maybe_attending'], merged_df['friends_invited'] = zip(*merged_df.apply(lambda row: get_friends_status(row, event_attendees_df), axis=1))
    # convert friends column to number of friends
    merged_df['friends'] = merged_df.apply (lambda row: count_words(row, 'friends'), axis=1)
    return merged_df

