# Care Emoji Generator Web App

A Flask web application that transforms images into cute "care emojis" with loving arms wrapped around them.

## Features

- 📤 **Image Upload**: Upload your own images (JPG, JPEG, PNG)
- 📚 **ISBN Integration**: Generate emojis from book covers using ISBN
- 🎨 **Modern UI**: Beautiful, responsive design with Bootstrap
- ⚡ **Fast Processing**: Quick emoji generation and download
- 📱 **Mobile Friendly**: Works great on all devices

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Web App**:
   ```bash
   cd web
   python main.py
   ```

3. **Open Your Browser**:
   Navigate to `http://localhost:5337`

## How to Use

### Option 1: Upload an Image
1. Click "Upload Image" on the home page
2. Select an image file from your computer
3. Preview your image
4. Click "Generate Care Emoji"
5. Download your custom emoji!

### Option 2: Use a Book ISBN
1. Click "Use ISBN" on the home page
2. Enter a 13-digit ISBN number
3. The app will fetch the book cover
4. Preview the book cover
5. Click "Generate Care Emoji"
6. Download your custom emoji!

## API Endpoints

- `GET /` - Home page
- `GET /upload-image` - Image upload form
- `POST /upload-image` - Handle image upload
- `GET /isbn` - ISBN form
- `POST /isbn` - Handle ISBN submission
- `GET /show-image/<filename>` - Preview uploaded image
- `POST /show-image/<filename>` - Generate emoji from image
- `GET /emoji/<filename>` - Download generated emoji

## Configuration

The app can be configured through environment variables:

- `SECRET_KEY` - Flask secret key for sessions
- `MAX_CONTENT_LENGTH` - Maximum file upload size (default: 1MB)

## File Structure

```
web/
├── app/
│   ├── __init__.py          # Flask app configuration
│   ├── routes.py            # URL routes and handlers
│   ├── static/tmp/          # Temporary uploaded files
│   └── templates/           # HTML templates
│       ├── base.html        # Base template with styling
│       ├── index.html       # Home page
│       ├── upload_image.html # Image upload page
│       ├── isbn.html        # ISBN input page
│       └── show_image.html  # Image preview page
├── images/
│   ├── emoji.png           # Base emoji image
│   └── arm.png             # Emoji arms overlay
├── main.py                 # Main application entry point
├── emojiGenerator.py       # Core emoji generation logic
└── bookHandler.py          # ISBN/book cover handling
```

## Technical Details

- **Framework**: Flask
- **Image Processing**: Pillow (PIL)
- **Book Data**: Google Books API
- **Frontend**: Bootstrap 5
- **File Handling**: Werkzeug

## Tips for Best Results

- Use clear, high-contrast images
- Square images work best
- Images with clear subjects (faces, objects) are ideal
- Keep file size under 1MB

## Error Handling

The app includes comprehensive error handling for:
- Invalid file types
- File size limits
- Missing images
- Invalid ISBNs
- API failures
- Server errors

## Development

To run in development mode:

```bash
export FLASK_ENV=development
python main.py
```

The app will run with debug mode enabled and auto-reload on code changes.