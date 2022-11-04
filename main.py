import cv2
import socket
import pickle
import datetime

HOST = '192.168.101.32'
PORT = 2000
BUFFER_SIZE = 4096
ADDER = (HOST, PORT)

if __name__ == '__main__':
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
            dt = datetime.datetime.now()
            cv2.putText(frame, f"{dt.year}/{dt.month}/{dt.day}/{dt.hour}/{dt.minute}/{dt.second}", (10, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) == ord('q'):
                break
cv2.destroyAllWindows()
            