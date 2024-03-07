#!/usr/bin/python3
"""
A recursive function that queries Reddit API for the total number of subscribers.
"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the total number of subscribers."""
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    try:
        data = res.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, ValueError):
        return 0

if __name__ == "__main__":
    # Test with an existing subreddit
    existing_subreddit = "programming"
    result_existing = number_of_subscribers(existing_subreddit)
    print(f"Subscribers for {existing_subreddit}: {result_existing}")

    # Test with a non-existing subreddit
    non_existing_subreddit = "this_is_a_fake_subreddit"
    result_non_existing = number_of_subscribers(non_existing_subreddit)
    print(f"Subscribers for {non_existing_subreddit}: {result_non_existing}")
