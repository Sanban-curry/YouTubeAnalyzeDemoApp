import streamlit as st

def views_input():

    st.title('YouTube分析アプリ')

    st.sidebar.write('## クエリと閾値の設定')
    st.sidebar.write('### クエリの入力')

    query = st.sidebar.text_input('検索クエリを入力してください', 'Python 自動化')

    st.sidebar.write('### 閾値の設定')
    threshold = st.sidebar.slider('登録者数の閾値', 100, 30000, 10000)

    st.write('### 選択中のパラメータ')
    st.markdown(f"""
    - 検索クエリ: {query}
    - 登録者数の閾値: {threshold}
    """)
    return query, threshold

def view_return(results):
    st.write('### 分析結果', results)
    st.write('### 動画再生')

    video_id = st.text_input('動画IDを入力してください。')
    url = f'https://youtu.be/{video_id}'

    video_field = st.empty()
    video_field.write('こちらに動画が表示されます。')
    if st.button('ビデオ表示'):
        if len(video_id) > 0:
            try:
                video_field.video(url)
            except:
                st.error('適切な動画IDを表示してください。')
