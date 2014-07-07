__author__ = 'angie'
import os
import pylast


def load_credentials():
    # read YAML settings file into credentials dictionary
    credentials_file = "settings.yaml"
    if os.path.isfile(credentials_file):
        import yaml
        with open(credentials_file, "r") as f:
            credentials = yaml.load(f)
    else:
        print "Something is wrong with reading the file."  # very shallow error handling

    return credentials


def network_setup():
    """
    Sets up a LastFMNetwork object. This is all that is required for some API calls.get_user.
    (Most require authentication)
    """
    credentials = load_credentials()
    password_hash = pylast.md5(credentials['password'])
    network = pylast.LastFMNetwork(api_key=credentials['api_key'], api_secret=credentials['api_secret'],
                                   username=credentials['username'], password_hash=password_hash)

    return network


def get_user():
    """
    An authenticated user is required for a lot of the method calls in the Last.fm API
    """
    user = network_setup().get_authenticated_user()
    return user


def get_my_recommended_artists(user):
    """
    Gets the top recommended artists for the given authenticated user.
    """
    recommended_artists = user.get_recommended_artists(limit=20)
    for artist in recommended_artists:
        print network.get_artist(artist.name)


def get_my_top_artists(user, x):
    """
    Takes an authenticated user and returns the top x artists for that user.
    """
    top_artists = user.get_top_artists(period=pylast.PERIOD_12MONTHS, limit=x)
    return top_artists


def get_my_recommended_events(user, x):
    """
    Takes an authenticated user and returns the top x recommended events for that user in the format:
    Artist - City
    """
    recommended_events = user.get_recommended_events(limit=x)
    for event in recommended_events:
        print pylast.Event.get_headliner(event), '-', pylast.Event.get_venue(event).get_location()['city']


def get_top_similar_artists(network, user, num_artists, num_similar_artists):
    """
    Returns a dictionary containing top artists for a user and a corresponding list containing
    the top similar artists for each artist.
    """
    # grab top artists
    top_artists = get_my_top_artists(user, num_artists)
    top_similar = {}  # dict to hold {artist: [similar artists]} mapping
    # Add only the name of the artist to the list
    for artist in top_artists:
        artist_string = str(artist[0])
        top_similar[artist_string] = []  # create an empty list to hold the similar artist mapping
        for sa in network.get_artist(artist_string).get_similar(limit=num_similar_artists):
            similar_artist_string = str(sa[0])
            top_similar[artist_string].append(similar_artist_string)
    return top_similar