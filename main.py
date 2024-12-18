"""
PymonSays: A Memory Game
A modern adaptation of the classic Simon Says game with an interactive and colorful UI.

Features:
- Progressive difficulty scaling
- High-score tracking
- Visual and audio feedback
"""

import os
import random
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import pygame

# Initialize pygame mixer for audio
try:
    pygame.mixer.init()
except Exception as e:
    print(f"Error initializing pygame mixer: {e}")

# Base path (compatible with PyInstaller bundling)
BASE_PATH = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Load sound files dynamically
SOUNDS = {
    "red": os.path.join(BASE_PATH, "red.wav"),
    "green": os.path.join(BASE_PATH, "green.wav"),
    "blue": os.path.join(BASE_PATH, "blue.wav"),
    "yellow": os.path.join(BASE_PATH, "yellow.wav"),
}

# Attempt to load sounds
try:
    sounds = {color: pygame.mixer.Sound(path) for color, path in SOUNDS.items()}
except Exception as e:
    print(f"Error loading sounds: {e}")
    sounds = {}

class PymonSays(App):
    def build(self):
        # Game state variables
        self.sequence = []
        self.player_sequence = []
        self.score = 0
        self.high_score = 0
        self.base_delay = 0.5

        # Main layout
        main_layout = BoxLayout(orientation="vertical", spacing=10)

        # Labels for game status and scores
        self.status_label = Label(text="Press Start to play!", font_size=20, size_hint=(1, 0.2))
        self.score_label = Label(text="Score: 0", font_size=16, size_hint=(1, 0.1))
        self.high_score_label = Label(text="High Score: 0", font_size=16, size_hint=(1, 0.1))
        main_layout.add_widget(self.status_label)
        main_layout.add_widget(self.score_label)
        main_layout.add_widget(self.high_score_label)

        # Buttons for the game
        self.buttons = {}
        colors = ["red", "green", "blue", "yellow"]
        button_layout = GridLayout(cols=2, spacing=10, size_hint=(1, 0.5))
        for color in colors:
            button = Button(
                background_color=self.get_button_color(color),
                text="",
                on_press=lambda instance, c=color: self.button_click(c)
            )
            self.buttons[color] = button
            button_layout.add_widget(button)
        main_layout.add_widget(button_layout)

        # Start button
        start_button = Button(text="Start", size_hint=(1, 0.1), on_press=self.start_game)
        main_layout.add_widget(start_button)

        return main_layout

    @staticmethod
    def get_button_color(color):
        # Returns the appropriate RGBA color for each button
        color_map = {
            "red": (1, 0, 0, 1),
            "green": (0, 1, 0, 1),
            "blue": (0, 0, 1, 1),
            "yellow": (1, 1, 0, 1)
        }
        return color_map.get(color, (1, 1, 1, 1))

    def flash_button(self, color, delay):
        # Flash the button and play sound
        def restore_button(*_):
            self.buttons[color].background_color = self.get_button_color(color)

        if color in sounds:
            sounds[color].play()
        self.buttons[color].background_color = (1, 1, 1, 1)
        Clock.schedule_once(restore_button, delay)

    def play_sequence(self):
        # Play the sequence for the player to memorize
        self.status_label.text = "Watch the sequence!"
        delay = max(0.2, self.base_delay - (self.score * 0.02))
        for i, color in enumerate(self.sequence):
            Clock.schedule_once(lambda dt, c=color: self.flash_button(c, delay), i * (delay + 0.5))
        Clock.schedule_once(lambda dt: self.player_turn(), len(self.sequence) * (delay + 0.5))

    def add_to_sequence(self):
        # Add a random color to the sequence
        colors = list(self.buttons.keys())
        self.sequence.append(random.choice(colors))

    def player_turn(self):
        self.status_label.text = "Your turn!"

    def check_sequence(self):
        # Validate the player's sequence
        if self.player_sequence == self.sequence[:len(self.player_sequence)]:
            if len(self.player_sequence) == len(self.sequence):
                self.score += 1
                self.high_score = max(self.high_score, self.score)
                self.update_scores()
                self.player_sequence = []
                Clock.schedule_once(lambda dt: self.next_round(), 1)
            else:
                self.status_label.text = "Keep going!"
        else:
            self.status_label.text = "Game Over! Press Start to play again."
            self.sequence = []
            self.player_sequence = []
            self.score = 0
            self.update_scores()

    def button_click(self, color):
        # Handle button clicks by the player
        if not self.sequence:
            return
        self.player_sequence.append(color)
        self.flash_button(color, 0.2)
        self.check_sequence()

    def next_round(self):
        # Proceed to the next round
        self.add_to_sequence()
        self.play_sequence()

    def start_game(self, instance):
        # Start a new game
        self.sequence = []
        self.player_sequence = []
        self.score = 0
        self.update_scores()
        self.status_label.text = "Watch the sequence!"
        self.next_round()

    def update_scores(self):
        # Update score and high score labels
        self.score_label.text = f"Score: {self.score}"
        self.high_score_label.text = f"High Score: {self.high_score}"


if __name__ == '__main__':
    try:
        PymonSays().run()
    except Exception as e:
        print(f"An error occurred: {e}")
