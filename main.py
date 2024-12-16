import tkinter as tk
import random
from time import sleep
import pygame
import sys
import os

# Get the base path (compatible with PyInstaller bundling)
BASE_PATH = getattr(
    sys,
    '_MEIPASS',
    os.path.dirname(os.path.abspath(__file__))
    )

# Load sounds dynamically from the correct path
SOUNDS = {
    "red": os.path.join(BASE_PATH, "red.wav"),
    "green": os.path.join(BASE_PATH, "green.wav"),
    "blue": os.path.join(BASE_PATH, "blue.wav"),
    "yellow": os.path.join(BASE_PATH, "yellow.wav"),
}

# Initialize pygame mixer
pygame.mixer.init()
sounds = {color: pygame.mixer.Sound(path) for color, path in SOUNDS.items()}

# Initialize variables
sequence = []
player_sequence = []
buttons = {}
score = 0
high_score = 0
base_delay = 0.5  # Base delay for flashing buttons


# Add a delay for showing the sequence and play sound
def flash_button(color, delay):
    sounds[color].play()  # Play the corresponding sound
    buttons[color].config(bg="white")
    root.update()
    sleep(delay)
    buttons[color].config(bg=color)
    root.update()
    sleep(0.2)


# Add a new color to the sequence
def add_to_sequence():
    colors = list(buttons.keys())
    sequence.append(random.choice(colors))


# Play the current sequence
def play_sequence():
    # Adjust delay based on score
    delay = max(0.2, base_delay - (score * 0.02))
    for color in sequence:
        flash_button(color, delay)


# Check player's input
def check_sequence():
    global player_sequence, sequence, score, high_score
    if player_sequence == sequence[:len(player_sequence)]:
        if len(player_sequence) == len(sequence):
            score += 1  # Increment score for completing a sequence
            high_score = max(high_score, score)  # Update high score
            update_score_labels()
            status_label.config(text="Correct! Watch the next sequence.")
            player_sequence = []
            root.after(1000, next_round)
        else:
            status_label.config(text="Keep going!")
    else:
        status_label.config(text="Game Over! Press Start to play again.")
        player_sequence = []
        sequence = []
        score = 0  # Reset score
        update_score_labels()


# Start a new round
def next_round():
    add_to_sequence()
    play_sequence()
    status_label.config(text="Your turn!")


# Handle button clicks
def button_click(color):
    global player_sequence
    player_sequence.append(color)
    flash_button(color, 0.2)  # Fixed delay for player clicks
    check_sequence()


# Start game
def start_game():
    global sequence, player_sequence, score
    sequence = []
    player_sequence = []
    score = 0  # Reset score at the start
    update_score_labels()
    status_label.config(text="Watch the sequence!")
    next_round()


# Update the score and high score labels
def update_score_labels():
    score_label.config(text=f"Score: {score}")
    high_score_label.config(text=f"High Score: {high_score}")


# Create the GUI
root = tk.Tk()
root.title("Simon Says")

# Path to the icon
ICON_PATH = os.path.join(BASE_PATH, "icon.ico")
root.iconbitmap(ICON_PATH)  # Set the window icon

# Create status label
status_label = tk.Label(root, text="Press Start to play!", font=("Arial", 16))
status_label.pack(pady=10)

# Create score and high score labels
score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()
high_score_label = tk.Label(root, text="High Score: 0", font=("Arial", 14))
high_score_label.pack()

# Create the buttons
frame = tk.Frame(root)
frame.pack()

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    btn = tk.Button(
        frame,
        bg=color,
        width=10,
        height=5,
        command=lambda c=color: button_click(c)
    )
    btn.grid(
        row=0 if color in ["red", "green"] else 1,
        column=0 if color in ["red", "blue"] else 1
    )
    buttons[color] = btn

# Create the Start button
start_button = tk.Button(
    root, text="Start",
    command=start_game,
    font=("Arial", 14)
)
start_button.pack(pady=10)

root.mainloop()
