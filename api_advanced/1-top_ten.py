#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts listed for a given subreddit."""
__author__ = "espoir habimfura"
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyBot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
