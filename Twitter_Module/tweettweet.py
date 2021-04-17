import tweepy
import time

auth = tweepy.OAuthHandler('5jYpTbx5QifhpUk2FLYhH4CWT',
                           'kkL3XvtMJG72mgBtIUth6gUWorZHEvMKec1WqFLlTjNZ2nWpcu')
auth.set_access_token('346666789-6MAhW82LQBWqXYr4949yCbrjBfnCQV3pZtz9HZj7',
                      '13gGIyILh6uNepct60msio3dhQw5iDgt9CTrdJeGKsMpA')

api = tweepy.API(auth)
user = api.me()

# Generous bot


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1)


def followback():
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        print(follower.name)


followback()
