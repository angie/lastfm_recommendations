import lastfm
import echonest


# return Last.fm network object
network = lastfm.network_setup()
# authenticate a user to make Last.fm API calls
lastfm_user = lastfm.get_user()
# set up API key for The Echo Nest
en_credentials = echonest.load_credentials()

top_artists = lastfm.get_my_top_artists(lastfm_user)
for artist in top_artists:
    echonest.config.ECHO_NEST_API_KEY = echonest.load_credentials()
    print echonest.similar_artists(artist[0])