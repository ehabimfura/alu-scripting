#!/usr/bin/python3
"""fetches the title of all hot posts for a given subreddit recursively"""
__author__ = "espoir habimfura"
import re

# When checking each word in a title:
words = re.split(r'[ \t\n]', title.lower())  # split on spaces only
for word in words:
    if word == keyword:  # exact match only
        counts[keyword] += 1
