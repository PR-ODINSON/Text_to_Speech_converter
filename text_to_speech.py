#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize the TTS engine globally
engine = pyttsx3.init()

# Set default properties
engine.setProperty('rate', 175)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

def text_to_speech():
    """Convert text to speech."""
    text = text_input.get("1.0", "end-1c")  # Get text from Text widget
    if text.strip():
        engine.say(text)
        engine.runAndWait()
    else:
        messagebox.showerror("Error", "Text box is empty. Please enter some text.")

def save_audio():
    """Save the text as an audio file."""
    text = text_input.get("1.0", "end-1c")  # Get text from Text widget
    if text.strip():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".mp3",
            filetypes=[("Audio Files", "*.mp3"), ("All Files", "*.*")]
        )
        if file_path:
            engine.save_to_file(text, file_path)
            engine.runAndWait()
            messagebox.showinfo("Success", f"Audio saved as {file_path}")
    else:
        messagebox.showerror("Error", "Text box is empty. Please enter some text.")

# Create the main application window
app = tk.Tk()
app.title("Text to Speech Converter")
app.geometry("500x400")


# Add a label
tk.Label(app, text="Enter Text Below:", font=("Arial", 14)).pack(pady=10)

# Add a text input field
text_input = tk.Text(app, height=10, width=50, font=("Arial", 12))
text_input.pack(pady=10)

# Add buttons for TTS and saving audio
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Convert to Speech", command=text_to_speech, font=("Arial", 12), width=20).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Save as Audio File", command=save_audio, font=("Arial", 12), width=20).grid(row=0, column=1, padx=10)

# Run the application
app.mainloop()


# In[ ]:




