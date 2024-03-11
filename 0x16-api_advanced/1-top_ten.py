#!/usr/bin/python3
"""Fetch Data from reddit API"""
import requests


def top_ten(subreddit):
    """
    Get the titles of the first 10 hot posts
    listed for a given subreddit
    """

    u_agent = 'Mozilla/5.0'

    myheader = {
        'User-Agent': u_agent
    }

    headers = requests.utils.default_headers()
    headers.update(myheader)

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=headers).json()
    top_ten = r.get('data', {}).get('children', [])
    if not top_ten:
        print(None)
    for t in top_ten:
        print(t.get('data').get('title'))
