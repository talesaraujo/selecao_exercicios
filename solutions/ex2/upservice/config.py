import os

class Config:
    # Set up a path to save all the files
    FILE_UPLOADS = os.path.join(os.getcwd(), 'upservice/static/uploads')
    # Limit file extensions
    ALLOWED_EXTENSIONS = [".TXT", ".DOC", ".DOCX", ".ODT", ".WPD", ".TEX", ".RTF"]
    # Set up a maximum of of sixteen megabytes per upload
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
