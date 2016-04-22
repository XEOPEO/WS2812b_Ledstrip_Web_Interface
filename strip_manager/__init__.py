from flask import Flask
from flask_socketio import SocketIO

# Create Flask Application
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Create SocketIO server
socketio = SocketIO(app)

from . import views, errors, sockets, socketerrors
