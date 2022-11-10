import datetime
import pickle
import socket

import cv2

HOST = ''
PORT = 2000
BUFFER_SIZE = 4096
ADDER = (HOST, PORT)
VIDEO_PATH = 0
WINDOW_NAME = "frame"
SIZE = (640, 480)
VIDEO_NAME = "timelapse.mp4"
FRAME_RATE = 2

def init():
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')   
    video = cv2.VideoWriter(VIDEO_NAME, fourcc, 30, SIZE)
    dt = datetime.datetime.now()
    pre_ut = int(dt.timestamp())
    return fourcc, video, pre_ut


def show(frame):
    dt = datetime.datetime.now()
    cv2.putText(frame, f"{dt.year}/{dt.month}/{dt.day} {dt.hour}:{dt.minute}:{dt.second}",(10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow(f"{WINDOW_NAME}", frame)
    return dt
    

def timelapse(dt, pre_ut, frame, video):
    if ((int(dt.timestamp()) - pre_ut) > 1):
        video.write(frame) 
        pre_ut = int(dt.timestamp())
    return pre_ut
        

def main():
    fourcc, video, pre_ut = init ()
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketTCP:
            socketTCP.connect(ADDER)
            full_data = b''
            data = b''
            while True:
                data = socketTCP.recv(BUFFER_SIZE)
                if len(data) <= 0:
                    break
                full_data += data
            print(f"data = {len(full_data)}")
            frame = pickle.loads(full_data)
            
            dt = show(frame)
            
            pre_ut = timelapse(dt, pre_ut, frame, video)
            
            if cv2.waitKey(1) == ord('q'):
                break
    cv2.destroyAllWindows()
     
     
if __name__ == '__main__':
    main()

            
