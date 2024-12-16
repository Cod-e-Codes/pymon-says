import os
from pydub.generators import Sine
from pydub import AudioSegment
import pyttsx3

# Step 1: Generate tones
frequencies = {
    "red": 440,    # A4
    "green": 523,  # C5
    "blue": 659,   # E5
    "yellow": 784  # G5
}

# Dictionary to hold generated tone AudioSegments
tone_sounds = {}

for color, freq in frequencies.items():
    tone = Sine(freq).to_audio_segment(duration=500)  # 500ms tone
    tone_sounds[color] = tone

# Step 2: Generate voice sounds
engine = pyttsx3.init()

# Set higher-quality voice settings
engine.setProperty('rate', 150)  # Speed of speech (lower = slower)
engine.setProperty('volume', 1.0)  # Volume (1.0 = max)

# Optional: Choose a different voice (male/female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # (0 for male, 1 for female)

# Generate and save voice sounds
voice_files = {}
for color in frequencies.keys():
    voice_file = f"{color}_voice.wav"
    engine.save_to_file(color.capitalize(), voice_file)
    voice_files[color] = voice_file
engine.runAndWait()

# Step 3: Combine tones and voices
combined_sounds = {}

for color in frequencies.keys():
    # Load the voice sound using pydub
    voice = AudioSegment.from_file(voice_files[color])

    # Normalize audio to match loudness
    tone = tone_sounds[color].apply_gain(-20.0)  # Reduce tone volume
    voice = voice.apply_gain(-5.0)  # Reduce voice volume slightly

    # Resample to match sample rate (optional if mismatch occurs)
    tone = tone.set_frame_rate(44100)
    voice = voice.set_frame_rate(44100)

    # Combine tone and voice with overlay
    combined = tone.overlay(voice)

    # Save the combined sound
    combined_file = f"{color}.wav"
    combined.export(combined_file, format="wav")
    combined_sounds[color] = combined_file

print("Combined sounds saved:")
for color, file in combined_sounds.items():
    print(f"- {color}: {file}")

# Step 4: Cleanup temporary voice files
for voice_file in voice_files.values():
    try:
        os.remove(voice_file)  # Delete the temporary voice file
        print(f"Deleted temporary file: {voice_file}")
    except OSError as e:
        print(f"Error deleting file {voice_file}: {e}")
