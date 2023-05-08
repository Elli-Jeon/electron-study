from flask import Flask, request
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def welcome():
    print('Welcome')

@socketio.on('message')
def data_received(message):
    print(message)
    send(message)

@socketio.on('connect')
def connection():
    print('Echelon connection established')

if __name__ == '__main__':
    print("testing")
    socketio.run(app, port='8080', debug=True)