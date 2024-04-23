import streamlit as st
from PIL import Image # 파이썬 이미지 라이브러리
def main():
    # 1. 저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')
    st.image( img )
    st.image( img , width= 320)
    st.image( img , width= 500)
    st.image( img , use_column_width=True)

    # 2. 인터넷상에 있는 이미지를 화면에 표시하는 방법
    #    인터넷상의 이미지 : URL 이 있다 !!
    url_img = 'data:image/jpeg;base64,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'
    st.image(url_img,use_column_width=True)

    # 동영상 파일
    video_file = open('./data/video1.mp4','rb')
    st.video(video_file)

    # 오디오 파일
    audio_file = open('./data/song.mp3', 'rb')
    st.audio(audio_file, format='audio/mp3')
    

if __name__ == '__main__':
    main()