#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
__author__ = "espoir habimfura"
import requests

def top_ten(subreddit):
    """Queries Reddit API and prints titles of first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x01.api.advanced:v1.0.0 (by /u/espoir)"}
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print("None")
