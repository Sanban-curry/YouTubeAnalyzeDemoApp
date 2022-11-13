import models
import  views

def controll(youtube):
    query, threshold = views.views_input()
    df_video = models.video_search(youtube, query)
    df_data = models.get_channel_info(youtube, df_video)
    df_extracted = df_data[df_data["subscriber_count"] < threshold]
    results = models.get_video_info(youtube, df_extracted)
    results = models.change_line(results)
    views.view_return(results)