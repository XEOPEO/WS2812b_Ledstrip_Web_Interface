from flask import session, request
from . import socketio
from flask_socketio import emit, send

@socketio.on('connect')
def on_connect():
    print 'Strip controller connected'
    emit('command', 'NEW strip!', broadcast=True)
    
@socketio.on('disconnect')
def on_disconnect():
    print 'Strip controller disconnected'
    emit('command', 'Strip REMOVED!', broadcast=True)
    
@socketio.on('command')
def on_chat_message(data):
    emit('command', str(data), broadcast=True)
