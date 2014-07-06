# -*- coding: utf-8 -*-

import lastfm
import echonest


# return Last.fm network object
network = lastfm.network_setup()
# authenticate a user to make Last.fm API calls
lastfm_user = lastfm.get_user()
# set up API key for The Echo Nest
en_credentials = echonest.load_credentials()

# grab top artists
top_artists = lastfm.get_my_top_artists(lastfm_user, 20)
top_similar = {}  # dict to hold {artist: [similar artists]} mapping
# Add only the name of the artist to the list
for artist in top_artists:
    artist_string = str(artist[0])
    top_similar[artist_string] = []  # create an empty list to hold the similar artist mapping
    for sa in network.get_artist(artist_string).get_similar(limit=10):
        similar_artist_string = str(sa[0])
        top_similar[artist_string].append(similar_artist_string)