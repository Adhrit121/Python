#Made by ADHRIT THE GREAT
import os
import shutil
try:
    import time
    import keyboard
except Exception as e:
    print("\n\nError :"+str(e)+"\n\n")
    time.sleep(4)
    print("Cannot continue with code\n\n")
    time.sleep(8)




def clear():
    try:
        terminal_size = shutil.get_terminal_size()
        lines_to_print = terminal_size.lines
        for _ in range(lines_to_print):
            print(" ")
            time.sleep(0.05)
    except Exception as e:
        print("\n\nsmall error in clear() function:",e,"\n\ncontinuing with main code......")
        time.sleep(6)






time.sleep(1)
clear()
inpaaa=input("Enter text to send[default-(⌐▨_▨)]: ").strip()
print()
time.sleep(1)
numbr=input("\nNo of times to be sent[default-infinite]: ")
print()
time.sleep(1)
pause=input("\nTime to pause between sending each message[default-1.25]: ")
print()
time.sleep(1)
shutta=input("\nGo to sleep after sending?(Y/N)[default-N]: ")
print()
time.sleep(1)



if pause:
    pause=float(pause)
else:
    pause=1.25

if inpaaa:
    pass
else:
    inpaaa="(⌐▨_▨)"
time.sleep(1)
clear()
time.sleep(1)

nim=10
while True:
    print("Starting in "+str(nim)+"  ",end="\r")
    time.sleep(1)
    nim=nim-1
    if nim==0:
        break
print(" ")
time.sleep(0.7)
clear()
if numbr:
    numbr=int(numbr)
    print("Estimated time:",str(numbr*pause+20)+"sec     (may increase with large number of messages)")
    print(" ")
    time.sleep(7)
    clear()
    intra=0
    while numbr!=0:
        start_time = time.time()
        if intra%35==0:
            time.sleep(pause*5)
        time.sleep(pause)
        keyboard.write(inpaaa)
        keyboard.send("\n")
        numbr=numbr-1
        intra=intra+1
        print("Sent message "+str(intra)+" times       (time taken:"+str(time.time() - start_time)+")",end="\r")
        pause=pause+0.003
    print("                                                                                                                               ")
    time.sleep(2)
    print(" ")
    print("\nTotal times sent:"+str(intra))
else:
    intra=0
    print("Estimated time: infinite")
    print(" ")
    time.sleep(7)
    clear()
    intra=0
    while True:
        start_time = time.time()
        if intra%35==0:
            time.sleep(pause*5)
        time.sleep(pause)
        keyboard.write(inpaaa)
        keyboard.send("\n")
        intra=intra+1
        print("Sent message "+str(intra)+" times       (time taken:"+str(time.time() - start_time)+")",end="\r")
        pause=pause+0.003
    print("                                                                                                                               ")
    time.sleep(2)
    print(" ")
    print("\nTotal times sent:"+str(intra))




if "y" in shutta.lower():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0 ")

while True:
    time.sleep(9)
