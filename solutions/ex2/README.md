# file upload service

This is a Flask application that implements a service to upload very simple text files. A few extensions are supported. Do take in mind that document files containing way too complex content (such as images, tables, macros, etc) might not be accepted.

## Requirements
First off, install the dependencies
```bash
pip install -r requirements.txt
```

In order to debug, you will need to set up the 
following:
```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

Then you can run
```bash
flask run
```

## Usage
### Endpoints

` GET /files`

Lists all uploaded files and returns their quantity currently stored. 

`POST /uploads`

Sends a text file to the service. This file must have an acceptable extension (*.txt, *.doc, etc) and it must be sent as a multipart/form-data with a maximum size of 16MB, as well as properly identified by the attribute `documentFile`.
The service returns a json containing the file content.
