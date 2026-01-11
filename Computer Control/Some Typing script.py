#Made on 3/20/2024 at 10:37AM
# Uses the mouse position script to get the location of specific places on the screen. This script then moves the mouse to those positions so that it can type a string of changing letters

import pyautogui
import time

# Define positions
positions = [(2859, 620), (2583, 1012), (2166, 550), (3028, 1013), (2595, 854), (1883, 445), (1384, 53)]
num = "20ZZZZZZZZZ"

while True:
# Move to each position, click, and wait

    num = num + 1

    word = str(num)

    if num == 39:

       exit()   

    time.sleep(3)     

    pyautogui.moveTo(positions[0])
    pyautogui.click()
    time.sleep(20)

    pyautogui.moveTo(positions[1])
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(positions[2])
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(positions[3])
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(positions[4])
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1562, 378)
    pyautogui.typewrite(word)
    time.sleep(5)

    pyautogui.moveTo(positions[5])
    pyautogui.click()
    time.sleep(5)

    pyautogui.moveTo(positions[6])
    pyautogui.click()