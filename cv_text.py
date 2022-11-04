import sys
import datetime
import cv2

VIDEO_PATH = 0
WINDOW_NAME = "frame"

def init_video():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("cant open video")
        sys.exit()
    return cap


if __name__ == '__main__':
    cap = init_video()
    while True:
        ret, frame = cap.read()
        dt = datetime.datetime.now()
        cv2.putText(frame, f"{dt.year}/{dt.month}/{dt.day}/{dt.hour}/{dt.minute}/{dt.second}", (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(f"{WINDOW_NAME}", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
