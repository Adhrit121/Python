#this was used for creating the wordlist_num.txt file
try:
    import random
    list1 = list(range(1, 1000))
    list2 = list(range(999, 10000))
    list3 = list(range(9999, 100000))
    list4=  list(range(99999, 1000000))
    f = open("wordlist_num.txt", "a")
    random.shuffle(list1)
    random.shuffle(list2)
    random.shuffle(list3)
    random.shuffle(list4)
    for num in list1:
        f.write(str(num)+"\n")
    for num in list2:
        f.write(str(num)+"\n")
    for num in list3:
        f.write(str(num)+"\n")
    for num in list4:
        f.write(str(num)+"\n")
except:
    print("efref")




def portscan(host, type="fast"):
    if "fas" in type:
        fast=True
        add=list(range(1, 1025))
    else:
        print("\n"+colored("WARN","yellow")+" Deep scan takes several times more time to complete than a regular scan")
        time.sleep(5)
        print(" ")
        fast=False
        add=list(range(1, 65535))
    updating_print("Starting",colored(".","green"))
    ports=[7,20,21,22,23,25,53,69,80,135,143,587,989,990]
    random.shuffle(add)
    found=[]
    for port in add:
        if port in ports:
            continue
        else:
            ports.append(add)
    total=0
    now=0
    for port in ports:
        total=total+1
    for port in ports:
        now=now+1
        percent=now/total*100
        percent=str(percent).split(".")[0]
        s = socket.socket()
        try:
            s.connect((host, port),settimeout(0.2))
        except:
            print(colored(f"[{str(percent)}%] Trying-"+str(host)+":"+str(port),"red"), end=" ")
            print("                                                      ", end="\r")
            continue
        else:
            print(" ",end=" ")
            print(colored("[+] Found: "+str(host)+":"+str(port),"green"))
            app=str(host)+":"+str(port)
            found.append(app) #FAILED
































#FALED MISERABLI
def wyfy_control():
    print("Make sure ur connected to the router")
    ip=input("Enter ip of router:").strip()
    driver = webdriver.Chrome()
    driver.get("http://"+ip)
    yn=input("Password only/both:")
    element = driver.find_elements(By.CLASS_NAME, "text_field")

    # find number of input box
    print(len(element))

    # fill value in input box
    driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').send_keys("praveen")#f
    driver.find_element_by_xpath('//*[@id="RESULT_TextField-2"]').send_keys("yadav")
    driver.find_element_by_xpath('//*[@id="RESULT_TextField-3"]').send_keys("87871111")

    # check status
    x = driver.find_element_by_xpath('//*[@id="RESULT_TextField-1"]').is_displayed()
    print(x)
    driver.close()

#wyfy_elevate is just a new version of wyfy_control
def wyfy_elevate():
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0].strip()
    print("\n"+colored("Opening default gateway of router....","cyan"))
    time.sleep(4)
    print(colored("Check the login page if both username and password are required or only password is required","cyan")+"\n(opening login page in 10 seconds)\n")
    time.sleep(10)
    webbrowser.open(default_gateway)
    time.sleep(5)
    inpa=input("Options:\n   1.Only Password\n    2.Username and Password\nChoose option number: ")
    if "1" in inpa:
        print("Go back to the login page and click on the password input field\nThis code will start trying all passwords")
    else:
        print("Babba")
