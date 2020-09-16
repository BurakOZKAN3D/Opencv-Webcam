import cv2
import os
import numpy as np
import socket
import sys
import pickle
import struct
import acapture

cap=acapture.open(0)#cap=cv2.VideoCapture(0)
frames_per_seconds = 60.0
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(("localhost", 8080))

while True:
    ret,frame=cap.read()
    data = pickle.dumps(frame)
    message_size = struct.pack("<L", len(data))
    clientsocket.sendall(message_size + data)

if __name__ == '__main__':
	main()
