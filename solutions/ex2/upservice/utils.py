import os
from flask import current_app

def allowed_file(filename):
    _, file_ext = os.path.splitext(filename)

    if file_ext.upper() in current_app.config["ALLOWED_EXTENSIONS"]:
        return True

    return False
