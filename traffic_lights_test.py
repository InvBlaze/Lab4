from traffic_lights import TrafficLights
from time import sleep

# Initialize the TrafficLights object with GPIO pins
lights = TrafficLights(17, 27, 22)

# Test sequence
print("Testing Red light...")
lights.red_light()
sleep(2)

print("Testing Yellow light...")
lights.yellow_light()
sleep(2)

print("Testing Green light...")
lights.green_light()
sleep(2)

print("Test completed!")
