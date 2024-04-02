import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            
            if len(posts) > 0:
                print("Top 10 hot posts in r/{}:".format(subreddit))
                for post in posts[:10]:
                    print(post['data']['title'])
            else:
                print("No hot posts found in r/{}".format(subreddit))
        except Exception as e:
            print("Error parsing JSON response:", e)
            print("Response text:", response.text)
    else:
        print("Error:", response.status_code)
        print("Response text:", response.text)

# Test the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
