# Text-to-Speech (TTS) Converter

A simple graphical user interface (GUI) application built using Python for converting text to speech and saving it as an audio file. This project leverages the `pyttsx3` library for Text-to-Speech conversion and `tkinter` for the GUI.

## Features
- Convert any entered text to speech.
- Save the speech as an audio file in `.mp3` format.
- User-friendly interface for ease of use.

## Requirements
- Python 3.6+
- Required Python libraries:
  - `pyttsx3`
  - `tkinter`

## Installation
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install the required libraries:
   ```bash
   pip install pyttsx3
   ```
   Note: `tkinter` is typically included with standard Python installations. If it's missing, you can install it using your OS package manager.

## How to Use
1. Run the application:
   ```bash
   python app.py
   ```
2. Enter your text into the text box.
3. Click on:
   - **"Convert to Speech"** to hear the text spoken aloud.
   - **"Save as Audio File"** to save the text as an `.mp3` file. You'll be prompted to select a location to save the file.

## File Structure
- `app.py`: Main Python file containing the TTS converter code.

## Libraries Used
1. **pyttsx3**: A Text-to-Speech conversion library in Python.
2. **tkinter**: A built-in Python library for creating graphical user interfaces.

## Customization
You can modify the TTS properties in the code:
- **Speech Rate**: Adjust the speech speed by changing the `rate` parameter.
  ```python
  engine.setProperty('rate', 175)  # Speed of speech
  ```
- **Volume**: Adjust the volume by changing the `volume` parameter.
  ```python
  engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
  ```


## Contributions
Feel free to fork this repository, make improvements, and submit a pull request. Any suggestions or contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- Python and its amazing libraries.
- The open-source community for their contributions.


