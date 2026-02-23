#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:1-top_ten:v1.0 (by /u/espoir)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)
