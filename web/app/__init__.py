from flask import Flask
import os

app = Flask(__name__)

# Secret key for sessions (needed for flash messages)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'your-secret-key-here-change-in-production'

app.config["IMAGE_UPLOADS"] = "./app/static/"

app.config["IMAGE_FOLDER"] = "tmp"

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG"]

from app import routes
