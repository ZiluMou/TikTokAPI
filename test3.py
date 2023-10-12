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

popular_channels = {}

with TikTokApi() as api:
    api._get_cookies = get_cookies
    
# Fetch a large number of trending videos, say 500
    for trending_video in api.trending.videos(count=200):
     hashtags = [hashtag.name.lower() for hashtag in trending_video.hashtags]  # Assuming 'name' exists in each hashtag object
    
     if 'soccer' in hashtags or 'football' in hashtags or 'championsleague' in hashtags:
        username = trending_video.author.username  # Replace with the correct attribute if different
        if username not in popular_channels:
            popular_channels[username] = 0
        popular_channels[username] += 1  # Increment the count for the username

# Sort by popularity
sorted_channels = sorted(popular_channels.items(), key=lambda x: x[1], reverse=True)

# Print the most popular channels
for channel, count in sorted_channels[:10]:
    print(channel, count)


