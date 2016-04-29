from . import socketio
from flask_socketio import emit

@socketio.on('connect', namespace='/strip')
def on_connect():
    print 'Strip controller connected'
    
@socketio.on('disconnect', namespace='/strip')
def on_disconnect():
    print 'Strip controller disconnected'
    
@socketio.on('command', namespace='/strip')
def on_command(data):
    print data
    emit('command', str(data), broadcast=True)
