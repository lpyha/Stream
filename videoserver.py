import socketserver
import cv2
import pickle

HOST = '192.168.101.36'
PORT = 2000
BUFFER_SIZE = 4096
ADDER = (HOST, PORT)
cap = None

class MyTCPHandler(socketserver.BaseRequestHandler):
  def handle(self) -> None:
    ret, frame = cap.read()
    if not ret:
      print("cap error")
      exit()
    b_data = pickle.dumps(frame)
    self.request.send(b_data)
    
if __name__ == '__main__':
  cap = cv2.VideoCapture(0)
  if not cap.isOpened():
    print("cam error")
    exit()
  with socketserver.TCPServer((ADDER), MyTCPHandler) as server:
    server.serve_forever()
