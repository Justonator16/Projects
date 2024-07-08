#This project when run successfully moves mouse pointer to any random direction but wont click

import pyautogui as pag
import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)