__author__ = 'am'
import os

import pylast


def load_settings():
    # read YAML settings file
    settings_file = "settings.yaml"
    if os.path.isfile(settings_file):
        import yaml
        with open(settings_file, "r") as f:
            settings = yaml.load(f)
    else:
        print "Something is wrong with reading the file."  # very shallow error handling

    return settings


class Credentials:
    def __init__(self, settings):
        self.api_key = settings['api_key']
        self.api_secret = settings['api_secret']
        self.username = settings['username']
        self.password = settings['password']

    def setup(self):

        # create network object for interacting with Last.fm API
        self.network = pylast.LastFMNetwork(self.api_key, self.api_secret,
                                            self.username, self.password)

        return self.network


def get_my_recommended_artists():
    x = Credentials(load_settings())
    network = x.setup()
    user = network.get_user("omgangie")
    print user

print get_my_recommended_artists()