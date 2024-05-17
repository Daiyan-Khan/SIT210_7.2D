import os
import speech_recognition as sr
import RPi.GPIO as GPIO
import time


# GPIO setup for LED
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

def listen_for_command(audio_file):
    r = sr.Recognizer()
    
    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)  # Read the entire audio file
    
    try:
        command = r.recognize_sphinx(audio_data).lower()
        print("Recognized command:", command)
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

if __name__ == "__main__":
    try:
        # Listen for "on" command
        yes_command = listen_for_command("On.wav")
        if "on" in yes_command:
            turn_on_led()
        
        # Listen for "no" command
        no_command = listen_for_command("Off.wav")
        if "off" in no_command:
            turn_off_led()

    finally:
        GPIO.cleanup()  # Cleanup GPIO on program exit
