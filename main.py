"""  pip install pyautogui
    Parametry:
    interval (float): interval mezi kliknutími v sekundách.
    duration (float): doba, po kterou má být auto-clicker aktivní v sekundách.
"""
import pyautogui
import time

def autoclick(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)

if __name__ == "__main__":
    interval = float(input("Zadejte interval mezi kliknutími (v sekundách): "))
    duration = float(input("Zadejte dobu, po kterou chcete autoclicker spustit (v sekundách): "))
    print("Auto-clicker bude spuštěn za 10 vteřin. Přesuňte kurzor na místo, kde chcete klikat.")
    time.sleep(10)
    autoclick(interval, duration)
