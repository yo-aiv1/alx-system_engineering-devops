"""Fetch Data from reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Get subscribe count of a subreddit"""

    api = "https://www.reddit.com//r/{}/about.json".format(subreddit)
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}

    response = requests.get(api, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        JsonObj = response.json()
        return JsonObj["data"]["subscribers"]

    return 0
