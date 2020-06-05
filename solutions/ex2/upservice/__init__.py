import os
from flask import Flask
from upservice.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    # Import configs
    app.config.from_object(Config)

    # Create an upload folder
    if not os.path.exists(app.config['FILE_UPLOADS']):
        os.makedirs(app.config['FILE_UPLOADS'])

    # Register app main blueprint
    from upservice.main import main
    app.register_blueprint(main)

    return app
