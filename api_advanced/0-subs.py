#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""
__author__ = "espoir habimfura"
import requests

def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x01.api.advanced:v1.0.0 (by /u/espoir)"}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)
    return 0
