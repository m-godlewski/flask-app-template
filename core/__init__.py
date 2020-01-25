import core, config, flask, flask_restful, logging, logging.config, yaml

# logging configuration
logging.config.dictConfig(yaml.load(open(config.LOGGING_CONFIG_FILE)))

app = flask.Flask(__name__)
api = flask_restful.Api(app)

from core import routes