#!/usr/bin/python3
"""fetches the title of all hot posts for a given subreddit recursively"""
__author__ = "espoir habimfura"
import requests

def count_words(subreddit, word_list, found_list=None, after=None):
    """Parses titles of all hot articles and prints a sorted count of given keywords"""
    if found_list is None:
        found_list = {}
        for word in word_list:
            word_lower = word.lower()
            found_list[word_lower] = 0
            
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
            title_words = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                found_list[word_lower] += title_words.count(word_lower)
                
        if after is not None:
            return count_words(subreddit, word_list, found_list, after)
        else:
            sorted_counts = sorted(found_list.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print("{}: {}".format(word, count))
    else:
        return None
