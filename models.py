import pandas as pd


def video_search(youtube, q='Python Excel', max_results=50):

    response = youtube.search().list(
        q=q,
        part="id,snippet",
        order="viewCount",
        type="video",
        maxResults=max_results
    ).execute()

    items = response['items']
    items_id = []
    for item in items:
        item_id = {}
        item_id['video_id'] = item['id']['videoId']
        item_id['channel_id'] = item['snippet']['channelId']
        items_id.append(item_id)

    df_video = pd.DataFrame(items_id)
    return df_video


def get_channel_info(youtube, df_video):
    channel_ids = df_video['channel_id'].unique().tolist()

    sub_list = youtube.channels().list(
        id=','.join(channel_ids),
        part="statistics",
        fields='items(id, statistics(subscriberCount))',
    ).execute()

    sub_graph = []
    for item in sub_list['items']:
        sub = {}
        if len(item['statistics']) > 0:
            sub["channel_id"] = item['id']
            sub["subscriber_count"] = int(item['statistics']['subscriberCount'])
        else:
            sub["channel_id"] = item['id']
        sub_graph.append(sub)

    df_sub = pd.DataFrame(sub_graph)

    df_data = pd.merge(left=df_video, right=df_sub, on='channel_id')
    return df_data

def get_video_info(youtube, df_extracted):
    video_ids = df_extracted['video_id'].tolist()
    video_list = youtube.videos().list(
        id=video_ids,
        part="snippet, statistics",
        fields='items(id, snippet(title), statistics(viewCount))'
    ).execute()

    video_graph = []
    for item in video_list['items']:
        video = {}
        video["video_id"] = item['id']
        video["video_title"] = item['snippet']['title']
        video["view_count"] = int(item['statistics']['viewCount'])
        video_graph.append(video)

    df_video_data = pd.DataFrame(video_graph)

    results = pd.merge(left=df_extracted, right=df_video_data, on='video_id')
    return results

def change_line(results):
    results = results.loc[:, ['video_id', 'video_title', 'view_count', 'subscriber_count', 'channel_id']]
    return results

