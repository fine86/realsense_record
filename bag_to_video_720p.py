import pyrealsense2 as rs
import numpy as np
import cv2

# .bag 파일 경로
bag_file = "low/crane/turtlebot1.bag"

# Realsense 카메라 설정
config = rs.config()
config.enable_device_from_file(bag_file, repeat_playback=False)
#config.enable(stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline = rs.pipeline()
profile = pipeline.start(config)
playback = profile.get_device().as_playback()
playback.set_real_time(False)

# 비디오 저장을 위한 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 비디오 코덱 설정 (여기서는 XVID 사용)
color_video = cv2.VideoWriter('color_video2.avi', fourcc, 30, (640, 480))  # 저장할 비디오 파일 설정
depth_video = cv2.VideoWriter('depth_video2.avi', fourcc, 30, (640, 480), isColor=False)  # 저장할 비디오 파일 설정

count=0

try:
    while True:
        frames = pipeline.wait_for_frames()
        if not frames:
            break

        print(frames.get_timestamp())
        count = count + 1

        # Color 프레임 가져오기
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        # Depth 프레임 가져오기
        align = rs.align(rs.stream.color)
        aligned_frames = align.process(frames)

        depth_frame = aligned_frames.get_depth_frame()                
        depth_image = np.asanyarray(depth_frame.get_data())

        cv2.imshow('Depth Video', depth_image)

        depth_image = np.uint8(depth_image/256)

        # Color 및 Depth 비디오에 프레임 저장
        color_video.write(color_image)
        depth_video.write(depth_image)

        cv2.imshow('Color Video', color_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    color_video.release()
    depth_video.release()
    cv2.destroyAllWindows()
    print(count)
