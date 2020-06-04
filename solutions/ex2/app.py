import os

from flask import Flask
from flask import render_template, request, jsonify

app = Flask(__name__)

app.config.from_mapping(
    FILE_UPLOADS = "/home/talesaraujo/projects/selecao_exercicios/solutions/ex2/static/uploads",
    ALLOWED_EXTENSIONS = [".TXT", ".DOC", ".DOCX", ".ODT", ".WPD", ".TEX", ".RTF"]
)


def allowed_file(filename):
    _, file_ext = os.path.splitext(filename)

    print(file_ext.upper())

    if file_ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True

    return False


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files')
def files():
    filenames = os.listdir("static/uploads")
    return jsonify({"qtd_count": len(filenames), "uploaded_files": filenames})


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.files:
        document = request.files["documentFile"]

        if not document.filename:
            return jsonify({"error": "File must have a name."}), 403

        if not allowed_file(document.filename):
            return jsonify({"error": "This text document extension is not allowed."}), 403

        document.save(os.path.join(app.config["FILE_UPLOADS"], document.filename))

        with open(os.path.join(app.config["FILE_UPLOADS"], document.filename), "r") as uploaded_file:
            content = uploaded_file.read()

        return jsonify({
            "transaction_info": "File has been uploaded.",
            "filename": document.filename,
            "content": content
        }), 200

    return jsonify({"error": "A file must be provided"}), 404


if __name__ == "__main__":
    app.run(debug="True")
