from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, send
import socketio
from time import sleep
import json
import base64
import cv2
import logging
import serial


app = Flask(__name__)               #server initializations
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


def forward(data):              #Tank action control functions
    print(data)
    ser.write(str("1").encode('utf-8'))
    
def back(data):
    print(data)
    ser.write(str("2").encode('utf-8'))
    
def left(data):
    print(data)
    ser.write(str("3").encode('utf-8'))
    
def right(data):
    print(data)
    ser.write(str("4").encode('utf-8'))
    
def turret_left(data):
    print(data)
    ser.write(str("5").encode('utf-8'))
    
def turret_right(data):
    print(data)
    ser.write(str("6").encode('utf-8'))
    
def fire(data):
    print(data)
    ser.write(str("7").encode('utf-8'))
    
def stop(data):
    print(data)
    ser.write(str("8").encode('utf-8'))


@app.route('/')             #home route
def index():
    return render_template('index2.html')
    

@socketio.on('check')               #Live streaming event       
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
    

@socketio.on('action')              #Tank control event
def action_control(data):
        if data == '1':
            forward(data)
        elif data == '2':
            back(data)
        elif data == '3':
            left(data)
        elif data == '4':
            right(data)
        elif data == '5':
            turret_left(data)
        elif data == '6':
            turret_right(data)
        elif data == '7':
            fire(data)
        else:
            stop(data)


#@socketio.on('stop')
#def stop_motors(data):
#    print(data)
#    ser.write(str("8").encode('utf-8'))


if __name__ == "__main__":
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
