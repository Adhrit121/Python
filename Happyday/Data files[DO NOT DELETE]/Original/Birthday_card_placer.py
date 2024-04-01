import pymsgbox
import os
import time
from tkinter import *
from PIL import ImageTk,Image
import win32gui, win32con
import tempfile, base64, zlib
the_program_to_hide = win32gui.GetForegroundWindow()

#win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
# Backside Functions
def list_files(folder):
    try:
        import os
        all=os.listdir(folder)
        for fil in all:
            if ("." not in str(fil)):
                all.remove(fil)
        return all
    except:
        print("ERROR")

def copy(source,destination):
    try:
        import shutil
        x=shutil.copy(source,destination)
        print("File (",source,") copied as (",destination,")")
    except:
        args="Error in copying the file to (",destination,")"
        raise Exception (args)
        print("Error in copying the file to (",destination,")")

def popup(tex,title,style="none"):
    import tempfile, base64, zlib
    #Before using this plz make sure you import this: 'from tkinter import *'
    if style=="tkinter":

        ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
            'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))

        _, ICON_PATH = tempfile.mkstemp()
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(ICON)

        root = Tk()
        root.iconbitmap(default=ICON_PATH)
        root.title(title)
        root.geometry("500x200")
        label=Label(root,text=tex)
        label.pack()
        button=Button(root,text=" ᠎ Ok ᠎ ",bd = '5',command=root.destroy)
        button.pack(side=BOTTOM)
        root.mainloop()
    else:
        pymsgbox.alert(tex,title)

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
        return args
        raise Exception (args)




# Finder code
cwd=os.getcwd()
drive_folder = cwd[0:3]
user=get_current_user_name()
checr=drive_folder+user+'\\'
if os.path.isfile(checr+"Desktop")==True:
    onedrive=False
else:
    onedrive=True








# Frontside code


def card_true():
    popup("Hello :) \n\nBefore continuing, please rename your image as 'Hapba.png'  (in ''.png' format) \n\nFile will be detected upon changing the name to Hapba.png .....\n\nNOTE: Make sure the file is in the same folder as this"," ")
    he=0
    runs=0
    while True:
        runs=runs+1
        files_here=list_files(os.getcwd())
        for file in files_here:
            if "hapba" in file:
                name=file
                print(name,"detected")
                fil=name+" detected"
                popup(fil,"Detected")
                he=1
            elif "Hapba" in file:
                name=file
                print(name,"detected")
                fil=name+" detected"
                popup(fil,"Detected")
                he=1
        if runs>50:
            cut_off=1
            break
        if he==1:
            cut_off=0
            break
        time.sleep(3)


    if cut_off!=1:
        image_place=os.getcwd()+"\\"+name
        user=get_current_user_name()
        cwd=os.getcwd()
        drive_folder = cwd[0:3]
        destination=drive_folder+"Users\\"+get_current_user_name()+"\\Pictures\\"
        exe_place=cwd+"\\Data files[DO NOT DELETE]\\DATA FILES\\TYPE_OFF\\Google Chrome.exe"
        try:
            copy(image_place,destination)
            # End:
            copy(exe_place,cwd+"\\Output\\")
            if os.path.isfile(destination+name)==True:
                popa="Successfully completed... \n\nNow you can place the happy birthday card opener anywhere and it will work\n\nNOTE: The birthday card opener is in '"+cwd+"\Output"+"'"
                popup(popa,"Successful")
            else:
                message="ERROR \n\n "+"Unexpected error occurred :("
                popup(message, "Error")
        except Exception as e:
            message="ERROR: \n\n "+str(e)
            popup(message, "Error")
    elif cut_off!=0:
        popup("Timeout","Closing...")






def card_false():
    def after_name():
        name=name_var.get()
        cwd=os.getcwd()
        drive_folder = cwd[0:3]
        file_loc=drive_folder+"Users\\"+get_current_user_name()+"\\Pictures\\"+'name.txt'
        f = open(file_loc, "w")
        f.write(name)
        if os.path.isfile(file_loc)==True:
            popa="Successfully completed... \n\nNow you can place the happy birthday card opener anywhere and it will work\n\nNOTE: The birthday card opener is in '"+cwd+"\Output"+"'"
            popup(popa,"Successful")
            exe_place=cwd+"\\Data files[DO NOT DELETE]\\DATA FILES\\TYPE_ON\\Google Chrome.exe"
            copy(exe_place,cwd+"\\Output\\")
    popup("Hello :) \n\nNOTE: This requires an internet connection at the time of opening\n\nClick on 'OK' to continue"," ")
    import tempfile, base64, zlib
    #Before using this plz make sure you import this: 'from tkinter import *'
    ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
        'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, 'wb') as icon_file:
        icon_file.write(ICON)
    root = Tk()
    root.iconbitmap(default=ICON_PATH)
    root.title("Name")
    root.geometry("500x200")
    label=Label(root,text="Please enter name of person to who this is addressed to:")
    label.pack()
    name_var=StringVar(root)
    entry=Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    entry.pack()
    button=Button(root,text=" ᠎ Ok ᠎ ",bd = '5',command=lambda:[root.destroy(),after_name()])
    button.pack(side=BOTTOM)
    root.mainloop()




























def in_jpg():
    popup("Please rename the file into '.png' format to continue...... "," ")
ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
def yes():
    card_true()
def no():
    card_false()
root = Tk()
root.iconbitmap(default=ICON_PATH)
root.title(" ")
root.geometry("350x150")
label=Label(root,text="Hello :) \n\nDo you have the birthday card in .png format?")
label.pack()
button2=Button(root,text=" ᠎ Yes ᠎ ",bd = '7',command=lambda:[ root.destroy(),yes()])
button2.pack(side=BOTTOM)
button1=Button(root,text=" ᠎ No ᠎ ",bd = '5', command=lambda:[ root.destroy(),no()])
button1.pack(side=BOTTOM)
label=Label(root, fg="blue",text="I have the image in .jpg format")
label.pack(side=BOTTOM)
label.bind("<Button-1>", lambda e: in_jpg())
root.mainloop()
popup("Created By Adhrit","Done!! :)")
