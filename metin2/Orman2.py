import pyautogui
import time
import keyboard

from python_imagesearch import imagesearch


while True:
    time.sleep(1)
    metin = imagesearch.imagesearch("orman.PNG",0.4)

    if(metin==[-1,-1]):
        keyboard.press('E')
        time.sleep(0.5)
        keyboard.release('E')
        time.sleep(0.5)
        keyboard.press('F')
        time.sleep(1)
        keyboard.release('F')
        time.sleep(1)
    else:
        metin_x = metin[0]
        metin_y = metin[1]

        metin_x = metin_x + 45
        metin_y = metin_y + 50

        time.sleep(1)
        pyautogui.rightClick(metin_x, metin_y)

        time.sleep(1)
        pyautogui.leftClick(metin_x, metin_y)
        pyautogui.leftClick(metin_x, metin_y)
        pyautogui.leftClick(metin_x, metin_y)

        time.sleep(0.6)
        keyboard.press('A')

        time.sleep(0.6)
        keyboard.release('A')

        print(metin)

