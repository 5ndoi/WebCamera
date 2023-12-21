import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av
import cv2
from PIL import Image
import time

# 2023/12/19

# from process01 import to_app as wa
# import process01


previous_time = time.perf_counter() # [sec]


RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)


class VideoProcessor:
    def __init__(self) -> None:
        self.is_mirroring = True
        self.current_time = time.perf_counter()

    def recv(self, frame):
        image_cv = frame.to_ndarray(format="bgr24")

        image_height, image_width, channels = image_cv.shape[:3]

        # out_image_cv = process01.to_app(image_cv, self.is_mirroring)

        # cv2.putText(image_cv, "aaa", (20, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)

        # out_image_cv = cv2.cvtColor(cv2.Canny(image_cv, 100, 200), cv2.COLOR_GRAY2BGR)
        # cv2.putText(out_image_cv, "aaa", (20, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)
        # cv2.putText(image_cv, "aaa", (20, 20), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 1)
        
        self.current_time = time.perf_counter()

        return av.VideoFrame.from_ndarray(image_cv, format="bgr24")


webrtc_ctx = webrtc_streamer(
    key="example",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)

# if webrtc_ctx.video_processor:
#     webrtc_ctx.video_processor.is_mirroring = st.checkbox("Check the checkbox to flip horizontally.", value=True)
