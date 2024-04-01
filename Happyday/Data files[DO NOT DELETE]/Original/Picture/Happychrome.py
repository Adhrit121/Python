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




#Date of person's birthday(If bithday on march 31st then enter 31)
d3 = today.strftime("%d")
d4=d3.strip()
d4=int(d4)

root = Tk()
root.attributes('-fullscreen', True)
frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
try:
    image=Image.open(image_place)
    img = ImageTk.PhotoImage(image)
except Exception as e:
    mc="ERROR \n\n"+str(e)
    popup(mc,"ERROR")
    root.destroy
label = Label(frame, image = img)
label.pack()
btn = Button(root, text = 'Ok', bd = '15',command = root.destroy)
btn.pack(side=BOTTOM)
root.mainloop()


url="www.google.com"
time.sleep(1.5)
try:
    webbrowser.open(url)
except Exception as e:
    print("ERROR:   "+e)
time.sleep(3)
popup("From/By Adhrit",":)")
