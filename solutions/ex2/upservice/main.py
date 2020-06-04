import os

from flask import current_app, Blueprint, render_template, request, jsonify
from werkzeug.utils import secure_filename
from upservice.utils import allowed_file

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/files')
def files():
    filenames = os.listdir(current_app.config['FILE_UPLOADS'])
    return jsonify({"qtd_count": len(filenames), "uploaded_files": filenames})


@main.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.files:
        if "documentFile" not in request.files:
            return jsonify({"error": "Document file not provided"}), 404

        document = request.files["documentFile"]

        if not document.filename:
            return jsonify({"error": "File must have a name."}), 403

        if not allowed_file(document.filename):
            return jsonify({"error": "This text extension is not allowed."}), 403

        filename = secure_filename(document.filename)
        document.save(os.path.join(current_app.config['FILE_UPLOADS'], filename))

        with open(os.path.join(current_app.config['FILE_UPLOADS'], filename), "r") as uploaded_file:
            content = uploaded_file.read()

        return jsonify({
            "transaction_info": "File has been uploaded.",
            "filename": filename,
            "content": content
        }), 200

    return jsonify({"error": "A file must be provided"}), 404
