"""
sound_gen.py: Generate and Combine Sounds for PymonSays

This script generates audio tones for the game buttons (red, green, blue, yellow)
and overlays them with synthesized voice prompts. The output is saved as `.wav` files
to be used in the PymonSays game.

Features:
- Generate pure sine wave tones for button sounds
- Use `pyttsx3` for text-to-speech voice synthesis
- Combine tones and voice prompts into a single `.wav` file per button
- Automatically clean up temporary files
"""

import os
from pydub.generators import Sine
from pydub import AudioSegment
import pyttsx3

# Output directory for generated files
OUTPUT_DIR = "sounds"

# Frequencies for button tones (in Hz)
FREQUENCIES = {
    "red": 440,    # A4
    "green": 523,  # C5
    "blue": 659,   # E5
    "yellow": 784  # G5
}

# Tone duration (in milliseconds)
TONE_DURATION = 500


def generate_tone(frequency, duration):
    """
    Generate a sine wave tone with the specified frequency and duration.
    
    Args:
        frequency (int): Frequency of the tone in Hz.
        duration (int): Duration of the tone in milliseconds.
    
    Returns:
        AudioSegment: The generated tone as an audio segment.
    """
    return Sine(frequency).to_audio_segment(duration=duration)


def synthesize_voice(text, filename):
    """
    Synthesize a voice prompt using pyttsx3 and save it to a file.
    
    Args:
        text (str): The text to be synthesized into speech.
        filename (str): The filename to save the synthesized speech.
    """
    engine = pyttsx3.init()

    # Configure voice settings
    engine.setProperty("rate", 150)  # Speed of speech (lower = slower)
    engine.setProperty("volume", 1.0)  # Max volume

    # Choose a voice (female by default)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)  # 0 = male, 1 = female

    # Save the synthesized voice to a file
    engine.save_to_file(text, filename)
    engine.runAndWait()


def combine_tone_and_voice(tone, voice_file, output_file):
    """
    Combine a tone and a voice file into a single audio file.
    
    Args:
        tone (AudioSegment): The tone audio segment.
        voice_file (str): Path to the voice file.
        output_file (str): Path to save the combined audio file.
    """
    # Load the voice audio
    voice = AudioSegment.from_file(voice_file)

    # Normalize volumes
    tone = tone.apply_gain(-20.0)  # Lower tone volume
    voice = voice.apply_gain(-5.0)  # Slightly lower voice volume

    # Combine the tone and voice with an overlay
    combined = tone.overlay(voice)

    # Save the combined audio
    combined.export(output_file, format="wav")


def clean_up_temp_files(temp_files):
    """
    Remove temporary files used during processing.
    
    Args:
        temp_files (list): List of temporary file paths to remove.
    """
    for file in temp_files:
        try:
            os.remove(file)
            print(f"Deleted temporary file: {file}")
        except OSError as e:
            print(f"Error deleting file {file}: {e}")


def main():
    """
    Main function to generate tones, synthesize voice prompts, and create
    combined audio files for the PymonSays game.
    """
    # Ensure the output directory exists
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Temporary files for voice prompts
    temp_voice_files = []

    # Process each button color
    for color, frequency in FREQUENCIES.items():
        try:
            # Generate tone
            print(f"Generating tone for {color}...")
            tone = generate_tone(frequency, TONE_DURATION)

            # Synthesize voice prompt
            voice_file = os.path.join(OUTPUT_DIR, f"{color}_voice.wav")
            print(f"Synthesizing voice for {color}...")
            synthesize_voice(color.capitalize(), voice_file)
            temp_voice_files.append(voice_file)

            # Combine tone and voice
            output_file = os.path.join(OUTPUT_DIR, f"{color}.wav")
            print(f"Combining tone and voice for {color}...")
            combine_tone_and_voice(tone, voice_file, output_file)

            print(f"Saved combined sound for {color}: {output_file}")
        except Exception as e:
            print(f"Error processing {color}: {e}")

    # Clean up temporary files
    print("Cleaning up temporary files...")
    clean_up_temp_files(temp_voice_files)

    print("Sound generation complete!")


if __name__ == "__main__":
    main()
