<!--<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>

 [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) -->

# Care Emoji Generator

> Transform any image into a cute "care emoji" with loving arms wrapped around it!

> The image files can be found at this [website](https://gamingph.com/2020/05/psd-download-for-facebook-care-emoji/).

## 🌐 Try It Online!

**🚀 [Live Web App](https://chromeshades.github.io/Care-Emoji-Generator/)** - Use it directly in your browser!

## 🎯 Multiple Ways to Use

### 1. **🌐 Web App (Recommended)**
- **Live Demo**: [https://chromeshades.github.io/Care-Emoji-Generator/](https://chromeshades.github.io/Care-Emoji-Generator/)
- No installation required
- Works on mobile and desktop
- Privacy-focused (images stay in your browser)

### 2. **💻 Command Line Interface**
- Perfect for automation and batch processing
- Supports both images and ISBN lookup

### 3. **🖥️ Local Flask Web App**
- Full-featured web interface
- ISBN support with Google Books API
- Run locally on your machine


[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger) [![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org) 


<!-- For more on these wonderful ~~badgers~~ badges, refer to <a href="http://badges.github.io/badgerbadgerbadger/" target="_blank">`badgerbadgerbadger`</a>.-->

![](images/banner.png)

> How does one use this script?

- Grab an interesting image
- Run the script
- Bang! You get your own "care emoji"!

<!--
> GIF Tools

- Use <a href="http://recordit.co/" target="_blank">**Recordit**</a> to create quicks screencasts of your desktop and export them as `GIF`s.
- For terminal sessions, there's <a href="https://github.com/chjj/ttystudio" target="_blank">**ttystudio**</a> which also supports exporting `GIF`s. 
-->
---

## Table of Contents

- [🌐 Online Web App](#-online-web-app)
- [💻 Command Line Usage](#-command-line-usage)
- [🖥️ Local Web App](#️-local-web-app)
- [Installation](#installation)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## 🌐 Online Web App

The easiest way to use the Care Emoji Generator! No installation required.

**➡️ [Try it now at GitHub Pages](https://chromeshades.github.io/Care-Emoji-Generator/)**

**Features:**
- ✅ Works in any modern browser
- ✅ Mobile-friendly responsive design
- ✅ Privacy-focused (images never leave your browser)
- ✅ Instant results
- ✅ No registration required

## 💻 Command Line Usage

Perfect for developers and automation!

### 🖥️ Local Web App

Want to run the full web interface locally? Great for development or if you need ISBN support.

**Quick Start:**
```bash
./start_webapp.sh
```

**Or step by step:**
```bash
cd web
python main.py
# Open http://localhost:5337
```

**Features:**
- 🌐 Beautiful web interface  
- 📤 Drag & drop image upload
- 📚 ISBN book cover integration
- 🔍 Real-time image preview  
- ⬇️ Automatic emoji downloads
- 🎨 Mobile-responsive design

---


---

## Installation

### Clone and Setup
1. Clone the repository:
```bash
git clone https://github.com/Chromeshades/Care-Emoji-Generator.git
cd Care-Emoji-Generator
```

2. (Recommended) Set up a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On macOS/Linux
# .venv\Scripts\activate   # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to the example folder to run the scripts:
```bash
cd example
```

---

## Examples

### 🖥️ Local Web App

For the full-featured local web interface:

```bash
# Start the Flask web app
./start_webapp.sh

# Or manually:
cd web
python main.py
```

Then open your browser to `http://localhost:5337`

**Features:**
- Beautiful web interface
- Image upload support
- ISBN book cover lookup
- Real-time preview
- Automatic downloads

### 💻 Command Line Interface

There is a file named `cli.py` in the `example/` folder. Open terminal and navigate to `example/`. Type the following:
```bash
python3 cli.py -h
```
It will print out usage and examples.

For example:

```bash
python3 cli.py ~/Downloads/cli_output.png --image gtm52.png
```

In this example, `~/Downloads/cli_output.png` will be the new image file while `gtm52.png` is the image that will be added to the emoji.

### 📓 Jupyter Notebook

There is a `Jupyter Notebook` named `interactive_example.ipynb` for you to use interactively.

---

## Contributing

> Star it!

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Chromeshades/Care-Emoji-Generator.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/Chromeshades/Care-Emoji-Generator/compare/" target="_blank">`https://github.com/Chromeshades/Care-Emoji-Generator/compare/`</a>.

---

<!-- ## Team

> Or Contributors/People

| <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> | <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> | <a href="http://fvcproductions.com" target="_blank">**FVCproductions**</a> |
| :---: |:---:| :---:|
| [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)    | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) | [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com)  |
| <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> | <a href="http://github.com/fvcproductions" target="_blank">`github.com/fvcproductions`</a> |

- You can just grab their GitHub profile image URL
- You should probably resize their picture using `?s=200` at the end of the image URL.

---

## FAQ

- **How do I do *specifically* so and so?**
    - No problem! Just do this.

--->

## Thanks
This file is created using this [template file](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46).

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
