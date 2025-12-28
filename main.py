import speech_recognition as sr
import webbrowser
import urllib.parse
import time

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        print("🎤 Voice Assistant Started")
        self.listen()

    def listen(self):
        while True:
            try:
                with self.microphone as source:
                    print("\nListening...")
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = self.recognizer.listen(source)

                command = self.recognizer.recognize_google(audio).lower()
                print("You said:", command)
                self.process_command(command)

            except sr.UnknownValueError:
                print("Could not understand")
            except KeyboardInterrupt:
                print("\nExiting...")
                break

    def process_command(self, command):

        if "exit" in command or "stop" in command:
            print("Goodbye 👋")
            exit()

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                webbrowser.open(
                    "https://www.google.com/search?q=" +
                    urllib.parse.quote(query)
                )

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        else:
            print("Command not recognized")

        time.sleep(1)


if __name__ == "__main__":
    VoiceAssistant()
