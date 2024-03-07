#!/usr/bin/python3
"""
A recursive function that queries the Reddit API for the total number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API """
    u_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent': u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    print(f"URL: {url}")
    print(f"Status Code: {res.status_code}")

    if res.status_code != 200:
        return 0

    dic = res.json()
    print(f"JSON Response: {dic}")

    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0

    return dic['data']['subscribers']

# Example usage:
subreddit_name = "programming"
result = number_of_subscribers(subreddit_name)
print(f"Subscribers for {subreddit_name}: {result}")
