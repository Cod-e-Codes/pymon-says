# PymonSays: A Mobile Memory Game

## Overview

PymonSays is a modern, mobile adaptation of the classic Simon Says memory game, built with **Kivy**. It features an interactive user interface, dynamic audio feedback, and progressive difficulty scaling for an engaging gameplay experience on Android.

---

## Key Features

- **Interactive Gameplay**: A colorful and responsive UI designed for touch-based devices.
- **Dynamic Audio Feedback**:
  - Unique tones for each button.
  - Voice-guided color prompts for immersive feedback.
- **Advanced Game Mechanics**:
  - Real-time score tracking.
  - Progressive difficulty scaling for a challenge.
  - High-score preservation.
- **Optimized Mobile Experience**:
  - Compatible with Android devices.
  - Lightweight and efficient, built with Kivy.

---

## Table of Contents
- [Releases](#releases) *(coming soon)*
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [How It Works](#how-it-works)
- [Dependencies](#dependencies)
- [Future Improvements](#future-improvements)
- [Screenshots](#screenshots) *(coming soon)*
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Releases

*Coming soon:*
- *Android `.apk` download*
- *iOS `.ipa` download*
<!--
### Latest Release

The latest APK file is available for download here:  
[**PymonSays v1.0 - Download APK**](https://github.com/Cod-e-Codes/python-simon-says/releases/tag/mobile-v1.0)

- **For Users**:  
  Download the `PymonSays.apk` file, transfer it to your Android device, and install it to start playing.

- **For Developers**:  
  Download the source code from the repository’s `mobile` branch. Follow the instructions below to run or modify the project. */

---
-->
## Prerequisites

### System Requirements
- **Platform**: Android
- **Python Version**: 3.8+ (for development and debugging)
- **Development Environment**:
  - **Kivy**: Cross-platform Python framework for GUI applications.
  - **Buildozer**: For packaging the app into an APK.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Cod-e-Codes/python-simon-says.git
cd python-simon-says
git checkout mobile
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Generate Sound Files (Optional)
Run the `sound_gen.py` script to regenerate the `.wav` sound files:
```bash
python sound_gen.py
```

### 4. Package the APK
Use Buildozer to package the app for Android:
```bash
buildozer -v android debug
```

The resulting APK will be located in the `bin/` directory.

---

## Usage

### On Android
- Install the APK on your Android device.
- Launch the app and follow the on-screen instructions.

### For Testing Locally
To test the app on your PC, run the following:
```bash
python main.py
```

Ensure all sound files (`.wav`) are present in the same directory as `main.py`.

---

## File Structure

```plaintext
pymonsays/
│
├── main.py              # Main game implementation (Kivy)
├── sound_gen.py         # Sound generation and management
├── requirements.txt     # Project dependencies
├── buildozer.spec       # Configuration for packaging the APK
│
├── sounds/              # Directory containing generated sound files
│   ├── red.wav
│   ├── green.wav
│   ├── blue.wav
│   └── yellow.wav
│
├── icon.png             # Application icon
├── README.md            # Project documentation
└── LICENSE              # License file
```

---

## How It Works

### 1. **Sound Generation** (`sound_gen.py`):
- Uses `pydub` to create pure sine wave tones.
- Synthesizes voice prompts with `pyttsx3`.
- Combines tones and voice prompts into `.wav` files for use in the game.

### 2. **PymonSays Game** (`main.py`):
- Built with **Kivy** for cross-platform support.
- Dynamic UI with responsive buttons and visual feedback.
- Progressive difficulty scaling and high-score tracking.

---

## Dependencies

| Library       | Version       | Purpose                        |
|---------------|---------------|--------------------------------|
| kivy          | >=2.0,<3.0    | Cross-platform GUI framework   |
| comtypes      | >=1.4.8,<2.0  | Windows COM interface (optional) |
| pydub         | >=0.25.1,<1.0 | Audio manipulation             |
| pygame        | >=2.6.1,<3.0  | Audio playback                 |
| pyttsx3       | >=2.98,<3.0   | Text-to-speech synthesis       |
| pywin32       | >=308,<309    | Windows Python extensions      |

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Future Improvements

- [ ] Add multiplayer mode for competitive play.
- [ ] Optimize performance for low-end Android devices.
- [ ] Add global leaderboards for score tracking.
- [ ] Customize sound themes for buttons and voices.

---

## Screenshots

*Coming soon: A preview of the game interface on mobile!*

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

For questions or feedback, contact:

- **Cody Marsengill**  
  Email: contact@cod-e-codes.com  

Project Link: [https://github.com/Cod-e-Codes/python-simon-says](https://github.com/Cod-e-Codes/python-simon-says)

---

**Enjoy challenging your memory with PymonSays!**
