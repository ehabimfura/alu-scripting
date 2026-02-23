#!/usr/bin/python3
"""Module to count keywords in hot posts of a given subreddit."""
import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keywords in hot post titles of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Pagination token for Reddit API.
        counts (dict): Accumulated keyword counts.

    Returns:
        None
    """
    if counts is None:
        counts = {}
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:count_words:v1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
    except requests.exceptions.RequestException:
        return

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words = re.split(r"[ \t\n]", title)
        for word in words:
            if word in counts:
                counts[word] += 1

    next_after = data.get("after")
    if next_after:
        count_words(subreddit, word_list, after=next_after, counts=counts)
    else:
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
