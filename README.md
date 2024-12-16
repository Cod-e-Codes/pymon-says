# Python Simon Says Game

## Overview

A modern, interactive implementation of the classic Simon Says memory game, featuring a responsive graphical user interface, dynamic sound effects, and engaging voice guidance.

## Key Features

- **Interactive Gameplay**: Responsive GUI with a classic Simon Says game mechanic
- **Dynamic Audio Experience**: 
  - Unique tones for each game button
  - Voice-guided color announcements
- **Advanced Game Mechanics**:
  - Comprehensive scoring system
  - Progressive difficulty scaling
  - High score tracking
- **Optimized User Experience**:
  - Clean, automated sound file management
  - Intuitive user interface

## Prerequisites

### System Requirements

- **Python Version**: 3.8+ (Tested on 3.12.3)
- **Platform**: Windows, macOS, Linux

### Development Tools

- Python
- pip
- (Recommended) Virtual environment

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Cod-e-Codes/python-simon-says.git
cd python-simon-says
```

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# macOS/Linux
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Getting Started

### Prepare Sound Files

```bash
python sound_gen.py
```

### Launch the Game

```bash
python main.py
```

## Project Architecture

### File Structure

```
python-simon-says/
│
├── main.py              # Primary game implementation
├── sound_gen.py         # Sound generation and management
│
├── *.wav                # Generated sound files
├── requirements.txt     # Project dependencies
├── screenshot.png       # Game interface preview
└── README.md            # Project documentation
```

## Technical Details

### Sound Generation

- Utilizes `pydub` for tone generation
- Leverages `pyttsx3` for voice synthesis
- Automatic cleanup of temporary audio files

### Game Mechanics

- Tkinter-based graphical interface
- Dynamic difficulty progression
- Real-time score tracking
- High score preservation

## Dependencies

| Library       | Version       | Purpose                        |
|---------------|---------------|--------------------------------|
| comtypes      | >=1.4.8,<2.0  | Windows COM interface          |
| pydub         | >=0.25.1,<1.0 | Audio manipulation             |
| pygame        | >=2.6.1,<3.0  | Audio playback                 |
| pypiwin32     | >=223,<224    | Windows Python extensions      |
| pyttsx3       | >=2.98,<3.0   | Text-to-speech synthesis       |
| pywin32       | >=308,<309    | Windows Python extensions      |

## Roadmap

### Upcoming Enhancements

- [ ] Implement visual button press effects
- [ ] Develop global leaderboard system
- [ ] Create custom sound theme support
- [ ] Cross-platform packaging solutions

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/Cod-e-Codes/python-simon-says](https://github.com/Cod-e-Codes/python-simon-says)

---

**Enjoy challenging your memory with Python Simon Says!**