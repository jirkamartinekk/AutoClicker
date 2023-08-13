import pyautogui
import time

def autoclick(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        try:
            pyautogui.click()
            time.sleep(interval)
        except KeyboardInterrupt:
            print("\nAuto-clicker byl ukončen.")
            break

if __name__ == "__main__":
    try:
        interval = float(input("Zadejte interval mezi kliknutími (v sekundách): "))
        duration = float(input("Zadejte dobu, po kterou chcete autoclicker spustit (v sekundách): "))
        print("Auto-clicker bude spuštěn za 5 vteřin. Přesuňte kurzor na místo, kde chcete klikat.")
        time.sleep(5)
        autoclick(interval, duration)
    except KeyboardInterrupt:
        print("\nAuto-clicker byl ukončen před spuštěním.")
