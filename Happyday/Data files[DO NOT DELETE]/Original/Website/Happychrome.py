import win32gui, win32con
the_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
from tkinter import *
from PIL import ImageTk,Image
import webbrowser
from datetime import date
import os
import time
def popup(text,title):
    import pymsgbox
    pymsgbox.alert(text=text, title=title)
today = date.today()
def get_current_user_name():
    def list_subfolders(folder_name_def):
        cwd=os.getcwd()
        subfolders=os.listdir(folder_name_def)
        drive_folder = cwd[0:3]
        for folder in subfolders:
            remove=0
            folder_name=str(folder)
            if ("$" in folder_name) or ("." in folder_name):
                subfolders = [ele for ele in subfolders if ele != folder]
        subfolders_with_paths=[]
        for folder in subfolders:
            full_path=drive_folder+"Users"+"\\"+folder
            subfolders_with_paths.append(full_path)
        folders=subfolders_with_paths
        return folders
    cwd=os.getcwd()
    drive_folder = cwd[0:3]
    drive=cwd[0:1]
    users=list_subfolders(drive_folder+"Users")
    file_name=__file__#Gives full path
    for folder in users:
        splitted=folder.split("\\")
        for word in splitted:
            if word in file_name:
                if word!="Users" and drive_folder not in word and drive not in word and "users" not in word:
                    user=word
                    done=1
    if done==1:
        return user
    else:
        args="ERROR"
        raise Exception (args)





cwd=os.getcwd()
cwd=str(cwd)
drive_letter = cwd[0]
drive_folder = cwd[0:3]
name=get_current_user_name()
users=drive_folder+"Users\\"+name+"\\Pictures\\"
image_place=users+"Hapba.png"










def is_cnx_active(timeout):
    try:
        import requests
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except Exception as e:
        print("ERROR:",e)
        return False










isl=is_cnx_active(2)
if isl==True:
    fileObject = open(os.path.join(users+"name.txt"), "r")
    data = fileObject.read()
    print(data)
    webbrowser.open("https://adhrit.vip/happy_bday.html?name="+data)
elif isl==False:
    popup("ERROR","ERROR")
