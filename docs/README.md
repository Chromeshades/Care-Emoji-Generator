# Care Emoji Generator - GitHub Pages Edition

A client-side web application that transforms images into cute "care emojis" with loving arms wrapped around them. This version runs entirely in the browser using HTML5 Canvas and JavaScript, making it perfect for GitHub Pages hosting.

## 🌐 Live Demo

Visit the live application: [https://chromeshades.github.io/Care-Emoji-Generator/](https://chromeshades.github.io/Care-Emoji-Generator/)

## ✨ Features

- 📤 **Client-Side Processing**: No server required - everything runs in your browser
- 🖼️ **Image Upload**: Supports JPG, PNG, GIF, WebP, and other image formats
- 🎨 **Real-Time Preview**: See your image before generating the emoji
- ⬇️ **Instant Download**: Generated emojis can be downloaded immediately
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- 🔒 **Privacy Focused**: Images never leave your browser
- ⚡ **Fast**: No server processing delays

## 🚀 How It Works

1. **Upload Image**: Choose any image from your device
2. **Preview**: See how your image will look
3. **Generate**: Click to create your care emoji
4. **Download**: Save your custom emoji to your device

## 🛠️ Technical Details

- **Frontend**: Pure HTML5, CSS3, and JavaScript
- **Image Processing**: HTML5 Canvas API
- **Styling**: Bootstrap 5
- **Hosting**: GitHub Pages (static hosting)
- **No Dependencies**: Works offline after initial load

## 📁 Project Structure

```
docs/                    # GitHub Pages source directory
├── index.html          # Main application file
├── emoji.png           # Base emoji image
└── arm.png             # Emoji arms overlay
```

## 🔧 Local Development

To run locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Chromeshades/Care-Emoji-Generator.git
   cd Care-Emoji-Generator
   ```

2. Serve the docs folder:
   ```bash
   # Using Python
   cd docs
   python -m http.server 8000
   
   # Using Node.js
   npx serve docs
   
   # Or just open index.html in your browser
   ```

3. Open your browser to `http://localhost:8000`

## 🆚 Differences from Flask Version

| Feature | Flask Version | GitHub Pages Version |
|---------|--------------|---------------------|
| **Hosting** | Requires Python server | Static hosting (GitHub Pages) |
| **ISBN Support** | ✅ (Google Books API) | ❌ (CORS limitations) |
| **Image Processing** | Server-side (Pillow) | Client-side (Canvas) |
| **File Upload** | Server upload | Browser-only |
| **Dependencies** | Flask, Pillow, requests | None |
| **Offline Support** | ❌ | ✅ (after initial load) |
| **Privacy** | Images sent to server | Images stay in browser |

## 🎯 Best Practices

- Use clear, high-contrast images for best results
- Square images work particularly well
- Faces and objects with clear outlines are ideal
- File size doesn't matter (processed locally)

## 🔄 Deployment

This version automatically deploys to GitHub Pages when you push to the main branch. The GitHub Actions workflow handles the deployment process.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes in the `docs/` directory
4. Test locally
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Original Flask version by the Care Emoji Generator team
- Bootstrap for the beautiful UI framework
- HTML5 Canvas API for client-side image processing