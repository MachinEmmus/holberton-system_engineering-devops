#!/urs/bin/python3
"""API ADVANCED"""

from requests import get


def number_of_subscribers(subreddit):
    """ subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {'User-Agent': 'Emmus'}
    response = get(url, headers=header).json()
    if response.get('data') and response.get('data').get('subscribers'):
        return (response['data']['subscribers'])
    return 0
