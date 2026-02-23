#!/usr/bin/python3
"""Module to query the Reddit API for top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python3:top_ten:v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
