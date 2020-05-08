#!/usr/bin/python3
"""API ADVANCED"""
from requests import get


def top_ten(subreddit):
    """API"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    header = {'User-Agent': 'Emmus'}
    response = get(url, headers=header, allow_redirects=False)
    if (response.status_code in [302, 404]):
        print(None)
    else:
        ten = response.json()['data']['children']
        count = 0
        for top in ten:
            if (count < 10):
                print(top['data']['title'])
            count += 1
