import os
import time
import threading
import pystray
from pystray import MenuItem as item
from PIL import Image
from pynput import keyboard

APPINDICATOR_ID = 'myappindicator'
ICON_PATH = '/home/xx/12.png'

def restart_service():
    os.system('sh /home/xx/restartservice.sh') #give a .sh path 

def build_menu():
    menu = (item('Restart', restart_service), item('Quit', lambda: exit()))
    return menu

def run_in_background():
    while True:
        time.sleep(60)

def on_press(key):
    try:
        if key == keyboard.Key.f8: #if press F8, restart the service
            restart_service()
    except AttributeError:
        pass

def main():
    icon = Image.open(ICON_PATH)
    menu = build_menu()
    icon = pystray.Icon(APPINDICATOR_ID, icon, "Title", menu)
    icon.run()

if __name__ == "__main__":
    threading.Thread(target=run_in_background).start()
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    main()
