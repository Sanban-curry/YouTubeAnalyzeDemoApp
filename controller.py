import models


def controll(youtube):

    df_video = models.video_search(youtube, 'python', 30) #検索の条件はviewから取得
    df_data = models.get_channel_info(youtube, df_video)
    df_extracted = df_data[df_data["subscriber_count"] < number] #numberはviewから取得
    results = models.get_video_info(youtube, df_extracted)
    results = models.change_line(results)
    print(results)