from TikTokApi import TikTokApi
import json

def get_cookies_from_file():
    with open('cookies.json') as f:
        cookies = json.load(f)

    cookies_kv = {}
    for cookie in cookies:
        cookies_kv[cookie['name']] = cookie['value']

    return cookies_kv

cookies = get_cookies_from_file()

def get_cookies(**kwargs):
    return cookies

with TikTokApi() as api:
    api._get_cookies = get_cookies
    for trending_video in api.trending.videos(count=10):
        print(trending_video.author.username)