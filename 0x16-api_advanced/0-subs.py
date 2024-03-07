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

    # Check for a successful response
    if res.status_code != 200:
        return 0

    try:
        data = res.json()

        # Check if the 'data' and 'subscribers' keys are present
        if 'data' in data and 'subscribers' in data['data']:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0

    except (KeyError, ValueError):
        return 0

if __name__ == "__main__":
    from subs import number_of_subscribers

    # Test with an existing subreddit
    existing_subreddit = "programming"
    result_existing = number_of_subscribers(existing_subreddit)
    expected_existing = 756024
    print(f"Subscribers for {existing_subreddit}: {result_existing}")
    print(f"Expected subscribers: {expected_existing}")
    print(f"Result matches expected: {result_existing == expected_existing}")

    # Test with a non-existing subreddit
    non_existing_subreddit = "this_is_a_fake_subreddit"
    result_non_existing = number_of_subscribers(non_existing_subreddit)
    expected_non_existing = 0
    print(f"Subscribers for {non_existing_subreddit}: {result_non_existing}")
    print(f"Expected subscribers: {expected_non_existing}")
    print(f"Result matches expected: {result_non_existing == expected_non_existing}")
