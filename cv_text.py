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



def create_timelapse():
    images = sorted("./timelapse/src/*.png") # 撮影した画像の読み込み。
    if len(images) < 30: #FPS設定
        frame_rate = 2  
    else:
        frame_rate = len(images)/30

    width = 640
    height = 480
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # 動画のコーデックをmp指定。（ちょっと違うが）動画の拡張子を決める、    
    video = cv2.VideoWriter("timelapse.mp4", fourcc, frame_rate, (width, height)) # 作成する動画の情報を指定（ファイル名、拡張子、FPS、動画サイズ）。


    for i in range(len(images)):
        # 画像を読み込む
        img = cv2.imread(images[i])
        # 画像のサイズを合わせる。
        video.write(img) 

    video.release()

def main():
    i = 0
    cap = init_video()
    dt = datetime.datetime.now()
    pre_ut = int(dt.timestamp())
    while True:
        ret, frame = cap.read()
        dt = datetime.datetime.now()
        cv2.putText(frame, f"{dt.year}/{dt.month}/{dt.day} {dt.hour}:{dt.minute}:{dt.second}",(10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow(f"{WINDOW_NAME}", frame)
        
        if (abs(pre_ut - int(dt.timestamp())) > 2):
            cv2.imwrite(f"./timelapse/src/{i}.png", frame)
            dt = datetime.datetime.now()
            pre_ut = int(dt.timestamp())
            i = i + 1
                
            
        if cv2.waitKey(1) == ord('q'):
            create_timelapse()
            break
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
