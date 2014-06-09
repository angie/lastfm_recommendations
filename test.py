__author__ = 'am'
import os
import sys
import time

import pylast


def load_settings():
    settings_file = "settings.yaml"
    if os.path.isfile(settings_file):
        import yaml
        with open(settings_file, "r") as f:
            settings = yaml.load(f)
    else:
        print "Something is wrong with reading the file."  # very shallow error handling

    return settings


def setup():
    settings = load_settings()

    # grab LastFMNetwork variables
    username = settings['username']
    password = settings['password']
    api_key = settings['api_key']
    api_secret = settings['api_secret']

    # create network object for interacting with Last.fm API
    network = pylast.LastFMNetwork(api_key=api_key, api_secret=api_secret,
                                   username=username, password_hash=password)

    return network

print setup()