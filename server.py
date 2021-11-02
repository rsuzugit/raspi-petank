from flask import Flask, render_template, request
import eventlet
import socketio
import eventlet.wsgi
import logging 
from time import sleep

sio = socketio.Server()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

logging.getLogger('socketio').setLevel(logging.ERROR)
logging.getLogger('engineio').setLevel(logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@sio.event()
def pingpong(sid):
    sio.emit("send_data", room=sid)
    
@sio.event 
def connect(sid, data):
    print("[INFO] Connect to the server")
    pingpong(sid)
    
@sio.on('send')
def send(sid, data):
    sio.emit('response', data)
    pingpong(sid)
    
@sio.event
def disconnect(sid):
    print("[INFO] disconnected from the server")
    
if __name__ == '__main__':
	eventlet.wsgi.server(eventlet.listen(('',5000)), app)

