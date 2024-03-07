#!/usr/bin/python3
"""
A script to query the Reddit API for the total number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API for the total number of subscribers."""
    user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': user_agent
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)

    # Debugging statements
    print(f"Status Code: {res.status_code}")
    print(f"Response Text: {res.text}")

    try:
        data = res.json()

        # Debugging statement
        print(f"JSON Data: {data}")

        # Check if the 'data' and 'subscribers' keys are present
        if 'data' in data and 'subscribers' in data['data']:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0

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
