

# Voice Assistant Using Speech Recognition and Text-to-Speech

This project implements a simple voice-controlled personal assistant in Python.
The assistant listens to spoken user commands, converts them to text, processes them, and responds using text-to-speech output.

The assistant can greet the user, speak the current time, search Wikipedia for people, and exit on command.

---

## 1. Features

The assistant currently supports the following capabilities:

* Speech recognition using microphone input
* Text-to-speech responses
* Time announcements
* “Who is …” queries using Wikipedia summaries
* Greeting based on time of day
* Exit on voice commands: *stop / exit / bye*

---

## 2. Technologies Used

| Component          | Library              |
| ------------------ | -------------------- |
| Speech recognition | `speech_recognition` |
| Text to speech     | `pyttsx3`            |
| Knowledge lookup   | `wikipedia`          |
| Date and time      | `datetime`           |

---

## 3. Requirements

Install dependencies before running the assistant:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install wikipedia
pip install pyaudio
```

> Note:
> On some systems, `pyaudio` must be installed separately (for example via system package manager or wheel file).

---

## 4. How It Works

1. Initializes text-to-speech engine
2. Greets user based on current time
3. Continuously listens to microphone input
4. Recognizes speech using Google Speech API
5. Processes commands such as:

   * “what is the time”
   * “who is Albert Einstein”
   * “what is your name”
6. Speaks responses back to the user
7. Stops when user says:

   * *stop*
   * *exit*
   * *bye*

---

## 5. Running the Program

Run the script:

```bash
python main.py
```

Make sure:

* a working microphone is connected
* internet connection is available (for speech recognition and Wikipedia lookup)

---

## 6. Microphone Configuration

The program uses microphone index:

```python
mic_id = 1
```

If your microphone index is different, list available microphones:

```python
import speech_recognition as sr
sr.Microphone.list_microphone_names()
```

Then update `mic_id` accordingly.


