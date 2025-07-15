import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init()
voice_options = engine.getProperty('voices')
engine.setProperty('voice', voice_options[0].id)
engine.setProperty('rate', 150)

def speak(text_to_say):
    print("Assistant:", text_to_say)
    engine.say(text_to_say)
    engine.runAndWait()

def say_hello():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I’m here to help. Just let me know what you need.")

def capture_voice_command():
    recognizer = sr.Recognizer()
    mic_id = 1
    user_query = ""

    try:
        print(f"Trying to use microphone at index {mic_id}...")
        with sr.Microphone(device_index=mic_id) as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            print("Okay, I’m listening now...")
            audio_data = recognizer.listen(mic)
            print("Trying to figure out what you said...")
            user_query = recognizer.recognize_google(audio_data)
            print(f"Captured: {user_query}")
            return user_query.lower()
    except sr.UnknownValueError:
        print("Speech was unclear...")
        speak("Hmm, I didn't catch that. Mind repeating?")
    except sr.RequestError as err:
        print("Issue reaching the speech API:", err)
        speak("Looks like there’s a network hiccup.")
    except Exception as general_error:
        print("Unexpected issue occurred:", general_error)
        speak("Something's off. Might wanna retry.")

    return ""

def main_loop():
    say_hello()

    while True:
        spoken_input = capture_voice_command()

        if spoken_input == "":
            continue

        if 'stop' in spoken_input or 'exit' in spoken_input or 'bye' in spoken_input:
            speak("Alrighty, talk soon!")
            break

        elif 'time' in spoken_input:
            now = datetime.datetime.now()
            formatted_time = now.strftime("%H:%M")
            speak(f"Current time is {formatted_time}")

        elif 'your name' in spoken_input:
            speak("They call me Vee. I’m your assistant buddy.")

        elif 'who is' in spoken_input:
            topic = spoken_input.replace("who is", "").strip()
            if topic:
                try:
                    summary = wikipedia.summary(topic, sentences=2)
                    speak(summary)
                except Exception as lookup_error:
                    print("Wiki lookup failed:", lookup_error)
                    speak("No luck finding anything on that.")
            else:
                speak("Could you tell me who you're asking about?")

        else:
            speak("I can tell you the time or look up a person. Try one of those?")

main_loop()
