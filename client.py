from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
import socketio
from time import sleep
import json
import base64
import cv2
import logging

logging.getLogger('socketio').setLevel(logging.ERROR)
logging.getLogger('engineio').setLevel(logging.ERROR)

cap = cv2.VideoCapture(0)
sio = socketio.Client(engineio_logger=False)

@sio.event
def connect():
	print("CONNECTED")

@sio.event
def send_data():
    
    while(cap.isOpened()):
        ret,img=cap.read()
        if ret:
            img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            frame = base64.encodebytes(frame).decode("utf-8")
            message(frame)
            sleep(0)
        else:
            break

def message(json):
	sio.emit('send', json)

@sio.event
def disconnect():
	print("DISCONNECTED")

if __name__ == '__main__':
	sio.connect('http://localhost:5000')
	sio.wait()
