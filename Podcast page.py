from flask import Flask, render_template
import feedparser

app = Flask(__name__)


@app.route('/')
def index():
    feed_url = "https://djw-podcast.nyc3.cdn.digitaloceanspaces.com/DJ_V4V_Podcast/feed.xml"
    feed = feedparser.parse(feed_url)
    cover_url = feed['feed']['image']['href']
    episodes = []

    for entry in feed.entries:
        title = entry.title
        description = entry.description
        audio_url = entry.enclosures[0]['url'] if entry.enclosures else ''
        episodes.append({'title': title, 'audio_url': audio_url})

    return render_template('index.html', cover_url=cover_url, episodes=episodes)


if __name__ == '__main__':
    app.run(debug=True)