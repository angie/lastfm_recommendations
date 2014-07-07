# -*- coding: utf-8 -*-

import lastfm
import echonest
from flask import Flask, render_template

# return Last.fm network object
network = lastfm.network_setup()
# authenticate a user to make Last.fm API calls
lastfm_user = lastfm.get_user()
# set up API key for The Echo Nest
en_credentials = echonest.load_credentials()

top_artists = lastfm.get_top_similar_artists(network, lastfm_user, 5, 10)
for a in top_artists:
    print a
    for sa in top_artists[a]:
        print '     %s' % sa


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html",
                           user=lastfm_user,
                           top_artists=top_artists)

if __name__ == '__main__':
    app.run()