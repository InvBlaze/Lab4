# SYSC3010 Lab 4 - Raspberry Pi GPIO and GitHub Collaboration

## Breadboard and Schematic Views:
- **Fixed GPIO Conflict Circuit**:
  - ![Breadboard View]
  - ![Schematic View]
- **I2C Sensor Circuit**:
  - ![I2C Sensor Breadboard]

## Description
- The **GPIO conflict issue** was fixed by moving the push button from **GPIO3** (conflicting with SenseHAT) to **GPIO4**.
- The **I2C sensor circuit** shows a BMP280 connected to RPi's **SDA (GPIO2) and SCL (GPIO3)**.

## Instructions
- Open these images in Fritzing to view the exact wiring.



## Overview
This part simulates a traffic light system using **Raspberry Pi GPIO**.

## Files
- **traffic_lights.py** - Defines a class to control Red, Yellow, and Green LEDs.
- **traffic_lights_test.py** - Tests the traffic light implementation.
- **crosswalk_simulation.py** - Implements a traffic light system with a crosswalk button.

## Hardware Setup
- **Red LED** - GPIO17 (Pin 11)
- **Yellow LED** - GPIO27 (Pin 13)
- **Green LED** - GPIO22 (Pin 15)
- **Push Button** - GPIO23 (Pin 16)

## How to Run
```bash
python3 traffic_lights_test.py
python3 crosswalk_simulation.py
