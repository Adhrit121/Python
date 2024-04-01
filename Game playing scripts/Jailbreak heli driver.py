import time
import keyboard
import random
listed=["w","s","a","d","e","w","s","a","d","e"]
times=["0.5","1","1.5","2","2.5","3","3.5","4","4.5","5"]
while True:
    key=random.choice(listed)
    sleeping=float(random.choice(times))
    print("KEY-",key,"        for",sleeping,"sec")
    keyboard.press(key)
    time.sleep(sleeping)  # Keep the key pressed for 3 seconds
    keyboard.release(key)
    keyboard.send(key)
    sleeping=float(random.choice(times))
    print("pausing for",sleeping,"seconds\n\n")
    time.sleep(sleeping)
