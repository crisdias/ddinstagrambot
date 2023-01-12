import re
import twitter

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




# run_video_tests(video_tests)
test_twt_link_extract()