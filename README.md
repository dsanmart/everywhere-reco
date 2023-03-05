# Everywhere recommendation
<img align="center" width="700" height="150" src="assets/logo.jpg" > 


#
# Introduction

Everywhere is a mobile app that promotes events for users. In order to enhance the user experience, we propose implementing a recommendation system to determine which events a user is likely to attend. The system will take into account historical data, such as clubs the user has already visited, as well as demographic information, such as gender and nationality, and music preferences. Additionally, the recommendation system will also try to recommend other users who might have similar preferences, thus helping users find and connect with new friends who share their interests.

# Methodology

The recommendation system will be based on a hybrid version type of collaborative and content based filtering  approach, which utilises past user behaviour to predict future preferences. The system will use a [Dataset](/docs/source/datasets.md) to analyse the user's past event attendance history, demographic information, and music preferences to suggest events that align with the user's interests.

#


## Create a virtual environment

```bash
python3 -m venv venv
```

## Activate the virtual environment

```bash
source venv/bin/activate
```

## Install the project package
```bash
pip install -e .
```