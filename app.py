from flask import Flask, render_template, request, redirect, url_for, json

import requests

app = Flask(__name__)

lyrics_endpoint = 'https://api.lyrics.ovh/v1/{}/{}'


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    lyrics = ""
    artist = ""
    song = ""

    if request.method == 'POST':
        artist = request.form['artist']
        song = request.form['song']

        r = requests.get(lyrics_endpoint.format(artist, song))

        lyrics = r.json()["lyrics"]

    return render_template('index.html', lyrics=lyrics, artist=artist, song=song)


if __name__ == '__main__':
    app.run()
