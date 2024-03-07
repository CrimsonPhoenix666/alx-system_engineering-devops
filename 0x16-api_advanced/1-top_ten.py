#!/usr/bin/python3
"""
A script to query the Reddit API and print the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts."""
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        print(None)
        return

    try:
        data = res.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get('data', {}).get('title', '')
            print(title)

    except (KeyError, ValueError):
        print(None)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
