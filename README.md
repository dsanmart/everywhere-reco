<img align="center" width="100%" src="./assets/logo.jpg" > 
<br>
<br>

# Everywhere Recommender Engine

Everywhere is a social network mobile app that promotes events for users. In order to enhance the user experience, we propose implementing a recommendation system to determine which events a user is likely to attend. The system will take into account historical data, such as clubs the user has already visited, as well as demographic information, such as gender and nationality, and music preferences. Additionally, the recommendation system will also try to recommend other users who might have similar preferences, thus helping users find and connect with new friends who share their interests.

The recommendation system has been integrated into the Everywhere app. In order to do this, we deploy a Databricks workflow that runs every week and uploads the most relevant events for every user to Azure Cosmos DB for fast retrieval.

## Recommender demo

<img src="./assets/everywhere_recommender.gif" width="150" />

<br>

# Authors
- [Pablo Ortega](https://github.com/pabloortegaa)
- [Diego Sanmartin](https://github.com/dsanmart)
- [Yahya Laraqui](https://github.com/yahyalrq)
- [Rayane Mazari](https://github.com/rayanmazari90)