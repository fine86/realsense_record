import pyrealsense2 as rs
import numpy as np
from time import time

directory = ""

###### camera 1
f_color_1 = open(f"{directory}/color_time_1.txt", "w")
f_depth_1 = open(f"{directory}/depth_time_1.txt", "w")

# 디바이스 파일 이름 (my_v4l2_device 또는 사용자가 설정한 이름)
serial_1 = 'f1182006'

# Realsense 카메라에 연결
pipe_1 = rs.pipeline()
config_1 = rs.config()
config_1.enable_device(serial_1)  # 디바이스 파일을 사용하여 Realsense 카메라 설정
config_1.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config_1.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config_1.enable_record_to_file(f'{directory}/turtlebot1.bag')
config_1.resolve(pipe_1)

profile_1=pipe_1.start(config_1) 

#color_sensor = profile.get_device().first_color_sensor()
#color_sensor.set_option(rs.option.global_time_enabled, 1)

depth_sensor_1 = profile_1.get_device().first_depth_sensor()
depth_sensor_1.set_option(rs.option.global_time_enabled, 1)
color_sensor_1 = profile_1.get_device().first_color_sensor()
color_sensor_1.set_option(rs.option.global_time_enabled, 1)


###### camrea 2
f_color_2 = open(f"{directory}/color_time_2.txt", "w")
f_depth_2 = open(f"{directory}/depth_time_2.txt", "w")

# 디바이스 파일 이름 (my_v4l2_device 또는 사용자가 설정한 이름)
serial_2 = 'f1182366'

# Realsense 카메라에 연결
pipe_2 = rs.pipeline()
config_2 = rs.config()
config_2.enable_device(serial_2)  # 디바이스 파일을 사용하여 Realsense 카메라 설정
config_2.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config_2.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config_2.enable_record_to_file(f'{directory}/turtlebot2.bag')
config_2.resolve(pipe_2)

profile_2=pipe_2.start(config_2)

#color_sensor = profile.get_device().first_color_sensor()
#color_sensor.set_option(rs.option.global_time_enabled, 1)

depth_sensor_2 = profile_2.get_device().first_depth_sensor()
depth_sensor_2.set_option(rs.option.global_time_enabled, 1)
color_sensor_2 = profile_2.get_device().first_color_sensor()
color_sensor_2.set_option(rs.option.global_time_enabled, 1)

###### camrea 3
f_color_3 = open(f"{directory}/color_time_3.txt", "w")
f_depth_3 = open(f"{directory}/depth_time_3.txt", "w")

# 디바이스 파일 이름 (my_v4l2_device 또는 사용자가 설정한 이름)
serial_3 = 'f1182473'

# Realsense 카메라에 연결
pipe_3 = rs.pipeline()
config_3 = rs.config()
config_3.enable_device(serial_3)  # 디바이스 파일을 사용하여 Realsense 카메라 설정
config_3.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config_3.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
config_3.enable_record_to_file(f'{directory}/turtlebot3.bag')
config_3.resolve(pipe_3)

profile_3=pipe_3.start(config_3)

#color_sensor = profile.get_device().first_color_sensor()
#color_sensor.set_option(rs.option.global_time_enabled, 1)

depth_sensor_3 = profile_3.get_device().first_depth_sensor()
depth_sensor_3.set_option(rs.option.global_time_enabled, 1)
color_sensor_3 = profile_3.get_device().first_color_sensor()
color_sensor_3.set_option(rs.option.global_time_enabled, 1)


count=0

try:
    while True:
        count = count + 1

        ###### camrea 1
        # 프레임을 기다림
        frame_1 = pipe_1.wait_for_frames()
        if not frame_1:
            break
        
        #frame_1.keep()
      
        color_frame_1 = frame_1.get_color_frame()
        #print(f'color_frame : {color_frame.get_timestamp()}')

        depth_frame_1 = frame_1.get_depth_frame()
        #print(f'depth_frame : {depth_frame.get_timestamp()}')

        f_color_1.write(str(color_frame_1.get_timestamp()) + '\n')
        f_depth_1.write(str(depth_frame_1.get_timestamp()) + '\n')

        print()

        ###### camrea 2
        frame_2 = pipe_2.wait_for_frames()
        if not frame_2:
            break
        
        #frame_2.keep()

        color_frame_2 = frame_2.get_color_frame()
        #print(f'color_frame : {color_frame.get_timestamp()}')

        depth_frame_2 = frame_2.get_depth_frame()
        #print(f'depth_frame : {depth_frame.get_timestamp()}')

        f_color_2.write(str(color_frame_1.get_timestamp()) + '\n')
        f_depth_2.write(str(depth_frame_1.get_timestamp()) + '\n')
        print()

        ###### camrea 3
        frame_3 = pipe_3.wait_for_frames()
        if not frame_3:
            break
        
        #frame_2.keep()

        color_frame_3 = frame_3.get_color_frame()
        #print(f'color_frame : {color_frame.get_timestamp()}')

        depth_frame_3 = frame_3.get_depth_frame()
        #print(f'depth_frame : {depth_frame.get_timestamp()}')

        f_color_3.write(str(color_frame_1.get_timestamp()) + '\n')
        f_depth_3.write(str(depth_frame_1.get_timestamp()) + '\n')
        print()

finally:
    # 사용이 끝난 후 pipeline 정리
    pipe_1.stop()
    pipe_2.stop()
    pipe_3.stop()
    print(count)
