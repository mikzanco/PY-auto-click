import pyautogui
import time

def click_mouse():
    while True:
        position = pyautogui.position()
        time.sleep(3)  # Pausa di 3 secondi
        if pyautogui.position() == position:  # Controlla se la posizione del mouse è rimasta la stessa
            pyautogui.click()  # Esegue il click del mouse

click_mouse()


