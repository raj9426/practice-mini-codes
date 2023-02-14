import pyautogui
from time import sleep
sleep(3)
while 1:
    xy = pyautogui.position()
    print(xy)
    sleep(5)
