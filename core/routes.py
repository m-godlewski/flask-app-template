from core import app, controller, logging
from flask import jsonify

@app.route('/', methods=['GET'])
def index():
    logging.info('LOGGING -> INDEX')
    return jsonify('Index'), 200