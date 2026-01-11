#Made on 11/22/2023 at 4:20 PM
#Gets the mouse position and displays it, is a supplement to my other computer control scripts that move the mouse to specific positions such as the "Some typing script"

import pyautogui
import time

while True:
    time.sleep(1)
    print (pyautogui.position())