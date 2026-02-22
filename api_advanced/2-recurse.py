#!/usr/bin/python3
"""fetches the title of all hot posts for a given subreddit recursively"""
__author__ = "espoir habimfura"
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Main function"""
    if hot_list is None:
        hot_list = []
        
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0x01.api.advanced:v1.0.0 (by /u/espoir)"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
                            
    if response.status_code == 200:
        data = response.json().get("data", {})
        after = data.get("after")
        posts = data.get("children", [])
        
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
            
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
