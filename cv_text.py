import sys
import datetime
import cv2

VIDEO_PATH = 0
WINDOW_NAME = "frame"
SIZE = (640, 480)
VIDEO_NAME = "timelapse.mp4"
FRAME_RATE = 2

def init_video():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("cant open video")
        sys.exit()
    return cap

def main():
    cap = init_video()
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')   
    video = cv2.VideoWriter(VIDEO_NAME, fourcc, 30, SIZE)
    dt = datetime.datetime.now()
    pre_ut = int(dt.timestamp())
    while True:
        ret, frame = cap.read()
        dt = datetime.datetime.now()
        cv2.putText(frame, f"{dt.year}/{dt.month}/{dt.day} {dt.hour}:{dt.minute}:{dt.second}",(10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(f"{WINDOW_NAME}", frame)
        
        if (abs(pre_ut - int(dt.timestamp())) > 2):
            video.write(frame) 
            dt = datetime.datetime.now()
            pre_ut = int(dt.timestamp())
                
        if cv2.waitKey(1) == ord('q'):
            cap.release()
            video.release()
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
