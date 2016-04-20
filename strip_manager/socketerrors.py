from . import socketio
from flask import request

# For debugging

@socketio.on_error() # Handles the default namespace
def error_handler(e):
    raise e
    
@socketio.on_error_default # Handles all namespaces without an explicit error handler
def default_error_handler(e):
    print request.event['message'] # "my error event"
    print request.event['args'] # (data,)
    raise e
