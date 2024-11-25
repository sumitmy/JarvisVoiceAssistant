import speech_recognition as sr
import pyttsx3
import webbrowser


recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(command):
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    elif "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn")
    elif "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    else:
        speak("Sorry, I didn't understand the command.")
if __name__ == "__main__":
    speak("Initializing jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word jarvis...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("jarvis is active, listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                processCommand(command)

        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")

