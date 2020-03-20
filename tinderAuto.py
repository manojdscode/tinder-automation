import pyautogui
import time
from random import seed
from random import randint

#pyautogui.position()
#To get a position of the like button
#pyautogui.displayMousePosition()

"""
#Random number generator
#Generate number from 1 to 10
seed(1)
for _ in range(0,10):
    value=randint(0,10)
"""
i = 0
while i<100:
    seed(1)
    for _ in range(0,10):
        value = randint(0,10)
        pyautogui.click(1284,855)
        time.sleep(value/2)
    i+=1