import speech_recognition as sr
import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said: " + command)
        return command
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""

def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED ON")

def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED OFF")

def process_command(command):
    if "on" in command:
        turn_on_led()
    elif "off" in command:
        turn_off_led()
    else:
        print("Command not recognized")

if __name__ == "__main__":
    while True:
        user_command = listen_for_command()
        if user_command:
            process_command(user_command)
