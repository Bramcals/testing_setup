import os

mydir = os.getcwd()  # would be the MAIN folder
mydir_tmp = mydir + "/scr"  # add the testA folder name
mydir_new = os.chdir(mydir_tmp)  # change the current working directory
mydir = os.getcwd()  # set the main directory again, now it calls testA
print("directory: " + mydir)
