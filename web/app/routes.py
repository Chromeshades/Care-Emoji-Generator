import os
import uuid
from io import BytesIO
from PIL import Image
import PIL
from flask import render_template, flash, redirect, url_for, request, send_from_directory, after_this_request, send_file
from app import app
from bookHandler import BookHandler
from emojiGenerator import EmojiGenerator
from werkzeug.utils import secure_filename

def splitExtension(s):
    t = s.rsplit(".", 1)
    return (t[0], t[1])

def getRandomName(ext):
    return str(uuid.uuid4())[-12:] + '.' + ext

def allowedImage(filename):
    if not "." in filename:
        return False

    _, ext = splitExtension(filename)

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route('/')
@app.route('/index')
def index():
    tmp_path = os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"])
    if not os.path.exists(tmp_path):
        os.makedirs(tmp_path)
    return render_template('index.html')

def allowedISBN(s):
    return s.isnumeric() if len(s) == 13 else False

@app.route('/isbn', methods=["GET", "POST"])
def isbn():
    if request.method == "POST":
        if request.form:
            isbn = request.form['isbn']
            if allowedISBN(isbn):
                try:
                    bh = BookHandler()
                    filename = getRandomName('png')
                    book_image = bh.getImageByISBN(isbn)
                    book_image.save(os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"], filename))
                    flash('Book cover found successfully!', 'success')
                    return redirect(url_for('show_image', filename=filename))
                except Exception as e:
                    flash(f'Error fetching book cover: {str(e)}', 'error')
                    return redirect(request.url)
            else:
                flash('Please enter a valid 13-digit ISBN.', 'error')
                return redirect(request.url)
    return render_template('isbn.html')

@app.route('/upload-image', methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                flash('Please select a file to upload.', 'error')
                return redirect(request.url)
            if allowedImage(image.filename):
                try:
                    _, ext = splitExtension(image.filename)
                    filename = getRandomName(ext)
                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], app.config["IMAGE_FOLDER"], filename))
                    flash('Image uploaded successfully!', 'success')
                    return redirect(url_for('show_image', filename=filename))
                except Exception as e:
                    flash(f'Error uploading image: {str(e)}', 'error')
                    return redirect(request.url)
            else:
                flash('Please upload a valid image file (JPG, JPEG, or PNG).', 'error')
                return redirect(request.url)
        else:
            flash('No file selected.', 'error')
            return redirect(request.url)
    return render_template('upload_image.html')

@app.route('/show-image/<filename>', methods = ["GET", "POST"])
def show_image(filename):
    if request.method == "POST":
        return redirect(url_for('emoji', filename=filename))
    full_name = os.path.join(app.config["IMAGE_FOLDER"], filename)
    return render_template("show_image.html", userfile = full_name)

def serve_pil_image(pil_img, filename="care_emoji.png"):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name=filename)

@app.route('/emoji/<filename>')
def emoji(filename):
    try:
        eg = EmojiGenerator()
        file_path = os.path.join(app.config['IMAGE_UPLOADS'], app.config["IMAGE_FOLDER"], filename)
        
        if not os.path.exists(file_path):
            flash('Image file not found.', 'error')
            return redirect(url_for('index'))
            
        img = Image.open(file_path)
        
        # Clean up the uploaded file
        try:
            os.remove(file_path)
        except Exception as error:
            app.logger.error(f"Error deleting file: {error}")
        
        t_filename, _ = splitExtension(filename)
        download_filename = f'care_emoji_{t_filename}.png'
        temp_img = eg.generateCareEmoji(img)
        
        return serve_pil_image(temp_img, download_filename)
        
    except Exception as e:
        app.logger.error(f"Error generating emoji: {str(e)}")
        flash(f'Error generating care emoji: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('File too large. Please upload an image smaller than 1MB.', 'error')
    return redirect(url_for('upload_image'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    flash('An internal error occurred. Please try again.', 'error')
    return redirect(url_for('index'))


