#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""
__author__ = "espoir habimfura"
import requests

def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0-subs:v1.0 (by /u/espoir)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
