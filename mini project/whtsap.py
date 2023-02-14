import pyautogui
import os
import time
import keyboard
import spotipy


def play_music(music):
    os.startfile("spotify")
    time.sleep(5)
    pyautogui.hotkey('ctrl','l')
    time.sleep(2)
    pyautogui.write(music, interval=0.1)
    time.sleep(1)
    pyautogui.click(x=559, y=337)
    time.sleep(2)
    pyautogui.click(x=390, y=486)
play_music("love today")