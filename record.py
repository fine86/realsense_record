import pyrealsense2 as rs
import numpy as np
from time import time

f_color = open("recorded/color_time.txt", "w")
f_depth = open("recorded/depth_time.txt", "w")

# 디바이스 파일 이름 (my_v4l2_device 또는 사용자가 설정한 이름)
device_serial = 'f1182366'

# Realsense 카메라에 연결
pipe = rs.pipeline()
config = rs.config()
config.enable_device(device_serial)  # 디바이스 파일을 사용하여 Realsense 카메라 설정
config.enable_stream(rs.stream.depth, 1024, 768, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)
config.enable_record_to_file('recorded/turtlebot1.bag')
config.resolve(pipe)

profile=pipe.start(config)

#color_sensor = profile.get_device().first_color_sensor()
#color_sensor.set_option(rs.option.global_time_enabled, 1)

depth_sensor = profile.get_device().first_depth_sensor()
depth_sensor.set_option(rs.option.global_time_enabled, 1)
color_sensor = profile.get_device().first_color_sensor()
color_sensor.set_option(rs.option.global_time_enabled, 1)


time_before = 0

count=0
try:
    while True:

        # 프레임을 기다림
        frames = pipe.wait_for_frames()
        if not frames:
            break
        
        frames.keep()
      
        count = count + 1

        time_now = frames.get_timestamp()


#        if time_now != time_before and count == 1:
#            file.write(str(time_now) + '\n')
#            count = 0
#        if time_now == time_before:
#            count = count + 1

#        if count > 1:
#            print('Error!!')
#        time_before = time_now
        #print(f'{count} : {frames.get_timestamp()}')


        color_frame = frames.get_color_frame()
        #print(f'color_frame : {color_frame.get_timestamp()}')

        depth_frame = frames.get_depth_frame()
        #print(f'depth_frame : {depth_frame.get_timestamp()}')

        f_color.write(str(color_frame.get_timestamp()) + '\n')
        f_depth.write(str(depth_frame.get_timestamp()) + '\n')


        print()
        #if depth_frame and color_frame:
        #color_data = np.uint8(color_frame.get_data())
        #depth_data = np.uint8(depth_frame.get_data())

        



finally:
    # 사용이 끝난 후 pipeline 정리
    pipe.stop()
    f_color.close()
    f_depth.close()

    print(count)
