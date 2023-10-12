from TikTokApi import TikTokApi
from time import sleep

def main():
    api = TikTokApi()
    video_id = '7260237357088001286'  # replace with your video's id
    while True:
        tiktok_dict = api.get_tiktok_by_id(video_id)
        view_count = tiktok_dict['itemInfo']['itemStruct']['stats']['playCount']
        print(f"Current view count: {view_count}")
        sleep(3600)  # pause for an hour

if __name__ == "__main__":
    main()
