__author__ = 'angie'
import os, pylast


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
    recommended_artists = user.get_recommended_artists(limit=20)
    for artist in recommended_artists:
        print network.get_artist(artist.name)


def get_my_recommended_events(user):
    recommended_events = user.get_recommended_events(limit=10)
    for event in recommended_events:
        print pylast.Event.get_headliner(event), '-', pylast.Event.get_venue(event).get_location()['city']