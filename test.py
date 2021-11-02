from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
import socketio
from time import sleep
import json
import base64
import cv2
import logging
import serial

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index1.html')


@socketio.on('check')
def gen(json):
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, img = cap.read()
        if ret:
            img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
            frame = cv2.imencode('.jpg', img)[1].tobytes()
            frame = base64.encodebytes(frame).decode("utf-8")
            message(frame)
            socketio.sleep(0)
        else:
            break


def message(json, methods=['GET', 'POST']):
    socketio.emit('image', json)


@socketio.on('forward')
def move_forward(data):
        if data == '1':
            print(data)
            ser.write(str("1").encode('utf-8'))


@socketio.on('stop')
def stop_motors(data):
    print(data)
    ser.write(str("8").encode('utf-8'))


if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    socketio.run(app, debug=True, host='127.0.0.1', port=5000)
