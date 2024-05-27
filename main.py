
import pyautogui

import time

#def klikaj_cyklicznie(x, y, interwal_czasowy, liczba_klikniec):
#    for _ in range(liczba_klikniec):
#        pyautogui.click(x, y)
#        time.sleep(interwal_czasowy)

# Przykładowe użycie:
x_pozycja = 500  # dostosuj do swoich potrzeb
y_pozycja = 300  # dostosuj do swoich potrzeb
interwal_czasowy = 10  # w sekundach, dostosuj do swoich potrzeb
liczba_klikniec = 5  # dostosuj do swoich potrzeb

#klikaj_cyklicznie(x_pozycja, y_pozycja, interwal_czasowy, liczba_klikniec)

from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        print('{} at {}'.format('Pressed Left Click' if pressed else 'Released Left Click', (x, y)))

    else:
        print('{} at {}'.format('Pressed Right Click' if pressed else 'Released Right Click', (x, y)))

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()