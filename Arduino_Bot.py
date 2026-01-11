# Made on 12/14/2024 at 8:55 PM
# Uses serial communication between the python script and a Arduino to control the angle of a servo using a keyboard. I made this to learn how to control arduino projects from my computer so that I could build a robot that used a Arduino as the brain of the robot to control everything and my computer to drive the robot around.

import serial
import keyboard
import time

# Configure the serial connection
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

print("Press 'u' to increase angle, 'd' to decrease angle, and 'q' to quit.")

try:
    while True:
        # Check if 'u' is pressed
        if keyboard.is_pressed('u'):
            arduino.write(b'u')  # Send 'u' to Arduino
            print("Sent: u")
        
        # Check if 'd' pressed
        if keyboard.is_pressed('d'):
            arduino.write(b'd')  # Send 'd' to Arduino
            print("Sent: d")
           
        
        # Exit the program if 'q' pressed
        if keyboard.is_pressed('q'):
            print("Exiting...")
            break
finally:
    arduino.close()