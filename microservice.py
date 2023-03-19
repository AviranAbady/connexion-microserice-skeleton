import logging.config
import os
import connexion
from config.logging import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

LOCAL_PORT = int(os.environ.get('MICROSERVICE_PORT', 0)) or 8080

app = connexion.FlaskApp(__name__, specification_dir="spec")
app.add_api("openapi.yaml")

if __name__ == "__main__":

    # Development only server start
    app.options.extend({"swagger_ui": True})
    app.run(debug=True,
            host='0.0.0.0',
            port=LOCAL_PORT)
