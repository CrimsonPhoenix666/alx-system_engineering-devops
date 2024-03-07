#!/usr/bin/python3
"""
Queries Reddit API and prints the titles of the first 10 posts
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        # Check if 'data' key is present and 'children' is not empty
        if 'data' in data and 'children' in data['data'] and data['data']['children']:
            for post in data['data']['children']:
                print(post['data']['title'])
        else:
            print(None)
    except (KeyError, ValueError):
        print(None)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])

