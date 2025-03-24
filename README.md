# Number-guessing-game
# Number Guessing Game

A simple Python game using Tkinter where users try to guess a randomly generated number within 10 attempts.

## Features
- Graphical User Interface (GUI) built with Tkinter
- Random number generation between 1 and 100
- Tracks previous best score
- Provides hints if the guessed number is too high or too low
- Restart and About options in the menu
- Image support for UI elements

## Requirements
- Python 3.x
- Required Libraries:
  - `tkinter` (built-in with Python)
  - `PIL` (Python Imaging Library, part of `Pillow` package)

## Installation
1. Clone this repository or download the source code.
2. Install dependencies using pip:
   ```sh
   pip install pillow
   ```
3. Ensure the following files are in the project directory:
   - `main.py` (the Python script)
   - `guess.png` (game icon/image)
   - `bt.jpeg` (button image, if used)
   - `score.txt` (to store high scores)

## How to Run
Run the Python script in PyCharm or terminal:
```sh
python main.py
```

## Troubleshooting
- **Image Not Displaying:** Ensure `guess.png` and `bt.jpeg` are in the same directory as `main.py`.
- **File Not Found Error:** Use absolute paths in Python to load images.
- **Tkinter Errors:** Make sure Python is installed correctly.

## About
Developed by **Surbhideep**. 

Enjoy the game! 🎮
