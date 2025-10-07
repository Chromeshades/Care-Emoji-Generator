<!--<a href="http://fvcproductions.com"><img src="https://avatars1.githubusercontent.com/u/4284691?v=3&s=200" title="FVCproductions" alt="FVCproductions"></a>

 [![FVCproductions](https://avatars1.githubusercontent.com/u/4284691?v=3&s=200)](http://fvcproductions.com) -->

# Care Emoji Generator

> This is a script for generating care-emoji.

> The image files can be found at this [website](https://gamingph.com/2020/05/psd-download-for-facebook-care-emoji/).


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

- [Example](#example)
- [Installation](#installation)
- [License](#license)


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

## Example

### Use `cli.py`

There is a file named `cli.py` in the `example/` folder. Open terminal and navigate to `example/`. Type the following:
```bash
python3 cli.py -h
```
It will print out usage and examples.

For example:

```
python3 cli.py ~/Downloads/cli_output.png --image gtm52.png
```

In this example, `~/Downloads/cli_output.png` will be the new image file while `gtm52.png` is the image that will be added to the emoji.

### Use `Jupyter Notebook`

There is a `Jupyter Notebook` named `interactive_example.ipynb` for you to use.

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
