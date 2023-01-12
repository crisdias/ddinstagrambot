import requests
import re

def get_canonical_url(url):
    # Use a regular expression to match URLs that start with "www" or "mobile"
    match = re.match(r'https?://(www|mobile)\.twitter\.com', url)
    if match:
        # If a match is found, replace "www" or "mobile" with "twitter"
        return url.replace(match.group(1) + '.', '')
    else:
        # If no match is found, return the original URL
        return url



def twt_is_video(url):
    # Use the canonical URL to check if the tweet is a video
    url = get_canonical_url(url)
    dlurl = url.replace('://twitter.com', '://dl.fxtwitter.com')

    id = url.split('/')[-1]
    r=requests.get(dlurl)

    return r.headers['Content-Type'] == 'video/mp4'

