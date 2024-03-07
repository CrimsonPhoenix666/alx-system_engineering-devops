#!/usr/bin/python3
"""
Queries Reddit API and prints the titles of the first 10 posts
"""
import requests


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 10
    }

    try:
        response = requests.get(url,
                                headers=headers,
                                params=params,
                                allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        results = response.json().get("data", {}).get("children", [])

        if not results:
            print(None)
        else:
            for post in results:
                title = post['data']['title']
                print(title)

    except requests.RequestException as e:
        print(f"Error: {e}")
        print(None)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
