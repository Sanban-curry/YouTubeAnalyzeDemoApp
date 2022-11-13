import json

from googleapiclient.discovery import build

import controller

with open('secret.json') as f:
    secret = json.load(f)

DEVELOPER_KEY = secret["KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

def main():
    controller.controll(youtube)


if __name__ == '__main__':
    main()