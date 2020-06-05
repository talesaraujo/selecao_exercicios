import os

from flask import current_app, Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
from upservice.utils import allowed_file


# Register main blueprint to promote modularization
main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Renders a simple form with options to select and upload file. 
    """
    return render_template('index.html')


@main.route('/files')
def files():
    """
    Returns a json file containing the info about file status
    """
    filenames = os.listdir(current_app.config['FILE_UPLOADS'])
    return jsonify({"qtd_count": len(filenames), "uploaded_files": filenames})


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Performs the upload operation according to some security constraints
    """
    if request.files:
        # Check if the request has the proper file part
        if "documentFile" not in request.files:
            return jsonify({"error": "Document file not provided"}), 404

        document = request.files["documentFile"]

        # Avoid submitting an empty part without filename
        if not document.filename:
            return jsonify({"error": "File must have a name."}), 403

        # Block unwanted file extensions to avoid XSS attacks
        if not allowed_file(document.filename):
            return jsonify({"error": "This text extension is not allowed."}), 403

        # Ensure not to allow dangerous user input
        filename = secure_filename(document.filename)
        document.save(os.path.join(current_app.config['FILE_UPLOADS'], filename))

        # Read content
        with open(os.path.join(current_app.config['FILE_UPLOADS'], filename), "r") as uploaded_file:
            content = uploaded_file.read()

        return jsonify({
            "transaction_info": "File has been uploaded.",
            "filename": filename,
            "content": content
        }), 200

    return jsonify({"error": "A file must be provided"}), 404
