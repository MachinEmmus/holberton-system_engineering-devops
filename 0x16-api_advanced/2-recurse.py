#!/usr/bin/python3
"""API ADVANCED"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?after='.format(subreddit)
    header = {'user-agent': 'Emmus'}
    response = get(url + str(after), headers=header, allow_redirects=False)
    if (response.status_code in [302, 404]):
        return(None)
    else:
        post = response.json()['data']['children']
        for top in post:
            hot_list.append(top['data']['title'])
        after = response.json()['data']['after']
        if (after is None):
            return (hot_list)
        return recurse(subreddit, hot_list, after)
