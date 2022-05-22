import shutil
import fnmatch
import os
directory = "raw_data"
des_directory = "final_data"
i = 0
for filename in os.listdir(directory):
    i += 1
    if fnmatch.fnmatch(filename, '*forward_left*'):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.forward_left.jpg")
    elif fnmatch.fnmatch(filename, '*forward_right*'):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.forward_right.jpg")
    elif fnmatch.fnmatch(filename, "*left*"):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.left.jpg")
    elif fnmatch.fnmatch(filename, "*right*"):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.right.jpg")
    elif fnmatch.fnmatch(filename, "*idle*"):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.idle.jpg")
    elif fnmatch.fnmatch(filename, "*forward*"):
        shutil.copy((directory + "/" + filename), f"{des_directory}/{i}.forward.jpg")
