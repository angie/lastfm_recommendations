__author__ = 'angie'
import os
from pyechonest import artist, config


def load_credentials():
    # read YAML settings file into credentials dictionary
    credentials_file = "en.yaml"
    if os.path.isfile(credentials_file):
        import yaml
        with open(credentials_file, "r") as f:
            credentials = yaml.load(f)
    else:
        print "Something is wrong with reading the file."  # very shallow error handling

    return credentials['API_KEY']


def similar_artists(search_artist):
    results = artist.search(name=search_artist)

    if results:
        r = results[0]
        print 'Artists similar to: %s:' % (r.name,)
        for similar in r.similar:
            print '     %s' % (similar.name,)
    else:
        print 'Artist not found'