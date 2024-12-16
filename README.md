# Python Simon Says

A modern twist on the classic Simon Says game implemented in Python. This project provides an interactive graphical user interface (GUI) using `tkinter`, generates dynamic sound effects with `pydub` and `pygame`, and incorporates voice guidance with `pyttsx3` for an engaging experience.

---

## Features
- **Interactive Gameplay**: Play the classic Simon Says game with a responsive GUI.
- **Dynamic Sounds**: Unique tones for each button using `pydub`.
- **Voice Prompts**: Button colors are announced via synthesized voice.
- **Scoring System**: Tracks the player's score and maintains a high score.
- **Increasing Difficulty**: Game speed increases as the player progresses.
- **Clean Design**: Temporary voice files are cleaned up automatically after use.

---

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Screenshot](#screenshot)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

---

## Prerequisites

- **Python 3.8+**: The project is tested on Python 3.12.3 but should work on versions 3.8 and above.
- **Pip**: Ensure you have pip installed for managing dependencies.
- **Virtual Environment**: (Recommended) Use a virtual environment to avoid conflicts with other Python projects.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cod-e-Codes/python-simon-says.git
   cd python-simon-says
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   .\venv\Scripts\activate   # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Generate the necessary sound files:
   ```bash
   python sound_gen.py
   ```

   This script creates `.wav` files for the game's tones and cleans up temporary voice files after combining them.

2. Start the game:
   ```bash
   python main.py
   ```

3. Enjoy the game! Follow the sequence of flashing buttons and try to beat your high score.

---

## File Structure

```plaintext
.
├── blue.wav           # Generated sound file for the blue button
├── green.wav          # Generated sound file for the green button
├── main.py            # Main script to run the Simon Says game
├── red.wav            # Generated sound file for the red button
├── requirements.txt   # List of dependencies
├── sound_gen.py       # Script to generate sound files
├── yellow.wav         # Generated sound file for the yellow button
├── screenshot.png     # Screenshot of the game in action
```

---

## How It Works

### 1. **Sound Generation** (`sound_gen.py`):
- Generates tones for the four colors using `pydub`.
- Synthesizes voice prompts for the colors using `pyttsx3`.
- Combines the tones and voice prompts into `.wav` files.
- Cleans up temporary voice files to keep the directory tidy.

### 2. **Simon Says Game** (`main.py`):
- Implements the Simon Says logic using `tkinter`.
- Plays the pre-generated sound files for feedback.
- Tracks the player's score and adjusts difficulty dynamically.
- Provides a high-score feature to encourage replayability.

---

## Dependencies

The project relies on the following Python libraries:

- `comtypes>=1.4.8,<2.0`
- `pydub>=0.25.1,<1.0`
- `pygame>=2.6.1,<3.0`
- `pypiwin32>=223,<224`
- `pyttsx3>=2.98,<3.0`
- `pywin32>=308,<309`

Install them using the provided `requirements.txt` file.

---

## Screenshot

![Screenshot of the game in action](screenshot.png)

---

## Future Improvements

- Add visual effects for button presses.
- Implement a leaderboard system for global high scores.
- Allow custom sound themes.
- Provide cross-platform packaging for standalone execution.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or bug fixes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the game and have fun challenging your memory!

