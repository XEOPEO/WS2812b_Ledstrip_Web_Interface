import logging
from flask import render_template
from . import app

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_errors(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(Exception)
def all_exceptions_handler(error):
    log.exception('Unhandled exception')
    return render_template('errors/500.html'), 500
