# Running Flask server

import os
from strip_manager import app, socketio

socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
