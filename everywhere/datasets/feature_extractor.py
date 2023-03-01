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

