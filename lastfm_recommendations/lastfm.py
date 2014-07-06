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