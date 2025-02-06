import RPi.GPIO as GPIO
import time

# Pin Definitions
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22
BUTTON_PIN = 23

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def set_light(red, yellow, green):
    GPIO.output(RED_PIN, red)
    GPIO.output(YELLOW_PIN, yellow)
    GPIO.output(GREEN_PIN, green)

def traffic_light_sequence():
    while True:
        print("Red Light - Stop")
        set_light(1, 0, 0)
        time.sleep(5)

        print("Green Light - Go")
        set_light(0, 0, 1)

        # Check for button press for 5 seconds
        for _ in range(50):
            if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
                print("Button pressed! Switching to Red...")
                set_light(0, 1, 0)
                time.sleep(2)
                set_light(1, 0, 0)
                time.sleep(5)
                break
            time.sleep(0.1)

        print("Yellow Light - Slow down")
        set_light(0, 1, 0)
        time.sleep(2)

try:
    traffic_light_sequence()
except KeyboardInterrupt:
    print("\nExiting program")
finally:
    GPIO.cleanup()
