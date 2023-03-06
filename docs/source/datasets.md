# Datasets for the Everywhere project

At first, we requested events and user data from applications like [Fourvenues](https://www.fourvenues.com/es) and [Guru it!](https://guruitapp.com/en/inicio). However, due to their unresponsiveness and delayed replies to our emails, we had to resort to utilizing a publicly accessible dataset. The [Kaggle Events Dataset](https://www.kaggle.com/competitions/event-recommendation-engine-challenge/data) we utilized was obtained from an anonymous events application that held a public competition several years ago. Here is a synopsis of the dataset elements we employed.

There are 6 datasets:

**1. Users**: Contains 38209 user_id, locale, birthyear, gender, joinedAt (when the user joined the app), location, and timezone. All users present in the train file contain demographic data.

**2. User friends**: Contains social data about 38202 users (user and list of friends).  user is the user's id in our system, and friends is a space-delimited list of the user's friends' ids.

**3. Events**: Contains information about 3137972 events with the columns: event_id, user_id (creator of the event), start_time, city, state, zip, country, latitude, and longitude. Along with these, the top 100 most frequently occurring words from event names and descriptions are provided for each of the events (obtained via Porter Stemming). In other words, a bag of words of size 100 is provided for each event as a representative of the event's name and description. Represented as count_1, count_2, ..., count_100, count_other where count_N is an integer representing the number of times the Nth most common word stem appears in the name or description of this event. count_other is a count of the rest of the words whose stem wasn't one of the 100 most common stems.

**4. Event attendees**: Contains information about which users attended various events, and has the following columns: event_id, yes, maybe, invited, and no. event_id identifies the event. yes, maybe, invited, and no are space-delimited lists of user id's representing users who indicated that they were going, maybe going, invited to, or not going to the event.

**5. Train**: Contains data on user_id, event_id, invitation (yes or no), timestamp (when the user first saw the event), interested & not_interested (boolean values indicating whether the user indicated that they were interested or not interested in the event).