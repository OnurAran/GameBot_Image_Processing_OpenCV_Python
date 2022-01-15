import pyautogui
import time
import keyboard

from python_imagesearch import imagesearch


#deger= input("Lütfen programı açmak için o tuşuna, kapatmak için c tuşuna basınız.")e
#if(deger== "o"):
    #deger=True
#else if(deger== "c"):
    #deger=False

while True:
    time.sleep(0.3)
    metin = imagesearch.imagesearch("katil_metini.PNG",0.4)
    can_bari = imagesearch.imagesearch("can_bari.PNG",0.4)

    if(metin==[-1,-1] or can_bari!=[-1,-1]):
        keyboard.press('E')
        time.sleep(0.3)
        keyboard.release('E')
        time.sleep(0.3)
        keyboard.press('F')
        time.sleep(0.3)
        keyboard.release('F')
        time.sleep(0.3)

        time.sleep(0.3)
        keyboard.press('D')

        time.sleep(0.3)
        keyboard.release('D')
        print("Metin Bulunamadı")
    else:
        metin_x = metin[0]
        metin_y = metin[1]

        metin_x = metin_x + 45
        metin_y = metin_y + 50

        time.sleep(0.3)
        pyautogui.rightClick(metin_x, metin_y)

        time.sleep(0.3)
        pyautogui.leftClick(metin_x, metin_y)

        time.sleep(0.4)
        keyboard.press('D')

        time.sleep(0.4)
        keyboard.release('D')



        print(metin)

