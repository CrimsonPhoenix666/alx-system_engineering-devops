#!/usr/bin/python3
"""
Queries Reddit API and prints the titles of the first 10 posts using recursion
"""
import requests


def add_title(hot_list, hot_posts):
    """ Adds item into a list """
    if len(hot_posts) == 0:
        return
    hot_list.append(hot_posts[0]['data']['title'])
    hot_posts.pop(0)
    add_title(hot_list, hot_posts)


def recurse(subreddit, hot_list=[], after=None):
    """ Queries Reddit API recursively """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json()
    hot_posts = data['data']['children']
    add_title(hot_list, hot_posts)
    after = data['data']['after']

    if not after or len(hot_list) >= 10:
        return hot_list

    return recurse(subreddit, hot_list=hot_list, after=after)


def top_ten(subreddit):
    """Top ten function using recursion"""
    hot_list = recurse(subreddit)
    
    if hot_list is None or len(hot_list) == 0:
        print(None)
    else:
        for title in hot_list[:10]:
            print(title)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
