# Made on 8/9/2024 at 8:39 AM
# A script that guesses passwords by constantly guessing passwords until it gets it correct. I built this because I had just learned in AP CSA how easy it is to guess passwords so in order to see this for myself I made this script.

import pyautogui
import random
import time


time.sleep(5)

pin = ""

list = [1,2,3,4]

letters_list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
for i in range (5000):
    for i in range (5):
        pin = pin + random.choice(letters_list)

    pyautogui.write(pin)
    pyautogui.press('backspace')
    pyautogui.press('enter')
    pin = ""




