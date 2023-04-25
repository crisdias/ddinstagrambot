import re
import twitter
from utils import *

valid_tiktok_urls = [
    "https://www.tiktok.com/@battlebots/video/7188169202467982635?_r=1&_t=8Zi6TBWysoI",
    "https://m.tiktok.com/@username/video/1234567890",
    "https://vm.tiktok.com/@username/video/1234567890",
    "https://tiktok.com/@username/video/1234567890",
    "https://vm.tiktok.com/ZMYjtF6tU/",
    "https://www.tiktok.com/t/ZTRtkbUqC/",
    "https://www.tiktok.com/t/ZTRtkbUqC"
]


valid_twitter_urls = [
    "https://twitter.com/elonmusk/status/1380000000000000000",
    "https://twitter.com/elonmusk/status/1380000000000000000?s=20",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000?s=20",
    "https://www.twitter.com/elonmusk/status/1380000000000000000",
    "https://www.twitter.com/elonmusk/status/1380000000000000000?s=20",
    "https://twitter.com/elonmusk/status/1380000000000000000/photo/1",
    "https://twitter.com/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000/photo/1",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://www.twitter.com/elonmusk/status/1380000000000000000/photo/1",
    "https://www.twitter.com/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://twitter.com/elonmusk/status/1380000000000000000/video/1",
    "https://twitter.com/elonmusk/status/1380000000000000000/video/1?s=20",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000/video/1",
    "https://mobile.twitter.com/elonmusk/status/1380000000000000000/video/1?s=20",
    "https://www.twitter.com/elonmusk/status/1380000000000000000/video/1",
    "https://www.twitter.com/elonmusk/status/1380000000000000000/video/1?s=20",
    "https://twitter.com/hankgreen/status/1613317341240258560"
]

invalid_twitter_urls = [
    "https://twitter.com/elonmusk/",
    "https://twitter.com/elonmusk",
    "https://mobile.twitter.com/elonmusk/",
    "https://mobile.twitter.com/elonmusk/",
    "https://www.twitter.com/elonmusk/",
    "https://www.twitter.com/elonmusk",

    "https://twitter.com/",
    "https://twitter.com",
    "https://mobile.twitter.com/",
    "https://mobile.twitter.com",
    "https://www.twitter.com/",
    "https://www.twitter.com",
]

twregex = re.compile(r'https?://(www\.)?(mobile\.)?twitter\.com/\w+/status/\d+')

for url in valid_twitter_urls:
    if not twregex.match(url):
        print(f"Failed to match valid: {url}")

for url in invalid_twitter_urls:
    if twregex.match(url):
        print(f"Matched invalid: {url}")


valid_nitter_urls = [
    "https://nitter.net/elonmusk/status/1380000000000000000",
    "https://nitter.net/elonmusk/status/1380000000000000000?s=20",
    "https://www.nitter.net/elonmusk/status/1380000000000000000",
    "https://www.nitter.net/elonmusk/status/1380000000000000000?s=20",
    "https://nitter.net/elonmusk/status/1380000000000000000/photo/1",
    "https://nitter.net/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://www.nitter.net/elonmusk/status/1380000000000000000/photo/1",
    "https://www.nitter.net/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://nitter.net/elonmusk/status/1380000000000000000/video/1",
    "https://nitter.net/elonmusk/status/1380000000000000000/video/1?s=20",
    "https://www.nitter.net/elonmusk/status/1380000000000000000/video/1",
    "https://www.nitter.net/elonmusk/status/1380000000000000000/video/1?s=20",
    "https://nitter.net/hankgreen/status/1613317341240258560",
    "https://nitter.net/jonesmanoel_PE/status/1649192103153418240"
]

invalid_nitter_urls = [
    "https://nitter.net/elonmusk/",
    "https://nitter.net/elonmusk",
    "https://mobile.nitter.net/elonmusk/",
    "https://mobile.nitter.net/elonmusk/",
    "https://www.nitter.net/elonmusk/",
    "https://www.nitter.net/elonmusk",

    "https://nitter.net/",
    "https://nitter.net",
    "https://mobile.nitter.net/",
    "https://mobile.nitter.net",
    "https://www.nitter.net/",
    "https://www.nitter.net",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000?s=20",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000/photo/1",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000/photo/1?s=20",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000/video/1",
    "https://mobile.nitter.net/elonmusk/status/1380000000000000000/video/1?s=20"
]

ntregex = re.compile(r'https?://(www\.)?nitter\.net/\w+/status/\d+')

for url in valid_nitter_urls:
    if not ntregex.match(url):
        print(f"Failed to match valid: {url}")

for url in invalid_nitter_urls:
    if ntregex.match(url):
        print(f"Matched invalid: {url}")



def run_video_tests(tests):
    for test in tests:
        print(f'\n\nChecking: {test}')
        print(twitter.twt_is_video(test))



video_tests = [
  'https://twitter.com/TVQuase/status/1613325938380472323',
  'https://twitter.com/felipeneto/status/1613411337882816512',
  'https://twitter.com/biosbug/status/1613556603915239424'
]






def test_twt_link_extract():
  message = "Please check out this tweet: https://mobile.twitter.com/username/status/1234567890, show of ball."

  url_match = twregex.search(message)
  if url_match:
      full_url = url_match.group()
      print(f'--{full_url}--')
  else:
      print("No URL found in message.")


def test_tiktok():
    ttregex = re.compile(r'https?://(www\.|m\.|vm\.)?tiktok\.com/(@[\w-]+/video/\d+|[\w-]+)(?:.*)(\?.*)?')


    for url in valid_tiktok_urls:
        ttmatch = re.search(ttregex, url)
        if ttmatch:
            xurl = ttmatch.group(0)
            # pp(xurl, "xurl")
            new_url = xurl.replace("tiktok.com/", "vxtiktok.com/")
            new_url = new_url.split("?")[0]
            print(f"Matched valid: {url} --> {new_url}")
        else:
            print(f"Failed to match valid: {url}")
    

# run_video_tests(video_tests)
test_tiktok()