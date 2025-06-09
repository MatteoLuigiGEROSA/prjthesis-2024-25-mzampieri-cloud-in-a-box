from flask import Flask, request, jsonify
from flask_restful import Api, Resource

import traceback

import urllib.parse

from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger

from utils.config import config, env
from utils.tracing.logger_utils import get_logger

# -----------------------------------------------------------------------------

# Inizializzazione logger flusso princilale Flask web-application (app_controller):
logger_name = "main_webapp_controller"
config_logger_level = config[env].APP_CONTROLLER_LOGGER_LOG_LEVEL
config_logger_mode = config[env].APP_CONTROLLER_LOGGER_LOG_CHANNELS

logger = get_logger(name=logger_name, level=config_logger_level, mode=config_logger_mode)

# -----------------------------------------------------------------------------

logger.info("$$$ START APPLICATION")

app = Flask(__name__)

# -----------------------------------------------------------------------------

# # Debug - stampa i parametri attuali della configurazione:
# print("-----  Configurazione attuale della web-application:  ----- -----")
# print(vars(config[env]))
# print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ")

# -----------------------------------------------------------------------------

# Creazione dell'API Flask-RESTful
api = Api(app)

# -----------------------------------------------------------------------------

cib_web_frontend_base_url = "/cib-web"
cib_rest_api_base_url = "/api/cib/v1.0.0"

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# --- Definizione Frontend web-site Endpoint(s)
# -----------------------------------------------------------------------------

@app.route('/')
def home():
    return "CFP G.Terragni di Meda, Project-Thesis CLOUD-IN-A-BOX (CIB) di Marco ZAMPIERI A.F. 2024-25 - Flask web-server per WEB-FRONTEND e REST-API"

# -----------------------------------------------------------------------------

# =============================================================================

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)

# =============================================================================
