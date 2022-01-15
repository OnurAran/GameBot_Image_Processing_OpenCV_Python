import pyautogui
import time
import keyboard
from python_imagesearch import imagesearch



while True:
    time.sleep(2)
    metin = imagesearch.imagesearch("karaorman.PNG",0.4)

    if (metin == [-1, -1]):
        time.sleep(2)
    else:
        metin_x = metin[0]
        metin_y = metin[1]

        metin_x = metin_x + 45
        metin_y = metin_y + 50

        for i in range(1):
            pyautogui.moveTo(metin_x, metin_y)
            pyautogui.click

        time.sleep(0.6)
        keyboard.press('A')

        time.sleep(0.6)
        keyboard.release('A')

        print(metin)