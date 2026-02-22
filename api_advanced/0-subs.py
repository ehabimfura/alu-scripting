#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""
__author__ = "espoir habimfura"
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
