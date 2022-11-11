#!/usr/bin/python

from googleapiclient.discovery import build

import json
with open('secret.json') as f:
    secret = json.load(f)
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = secret["KEY"]
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

q = 'Python'
max_results = 5
# def youtube_search(options):
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

response = youtube.search().list( #APIの関数などの機能を使うときはリファレンスを参照する。
    q=q,
    part="id,snippet",
    maxResults=max_results  #APIでして欲しい処理について詳細設定をして execute()で送信している。
).execute()

print(response)