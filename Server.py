import pickle
import socket
import struct
import cv2
import acapture
import time

server_address = ('localhost', 8080)
print('Start:',server_address)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connection established..')
s.bind((server_address))
s.listen(10)
print('Connection pending..')

conn, address = s.accept()
print('Connected:',address)

data = b'' 
payload_size = struct.calcsize("<L") 

prevTime = 0

while True:
    # Get the message size..
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("<L", packed_msg_size)[0] 

    # Get all data based on message size..
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Frame capture..
    frame = pickle.loads(frame_data)

    # Screen
    frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    cv2.imshow('Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()
