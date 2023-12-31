from sys import *
import os 
import time

def DirectoryTravel(DirName):
    print("We are going to scan the directory :",DirName)

    flag = os.path.isabs(DirName)

    if flag == False:
        DirName = os.path.abspath(DirName)

    exist = os.path.isdir(DirName)

    if exist:
        for foldername,subfoldername,filename in os.walk(DirName):
            print("Current directory name :",foldername)

            for subname in subfoldername:
                print("subfolder name is :",subname)

            for fname in filename:
                print(fname," : ",os.path.getsize(foldername+"/"+fname),"bytes")

    else:
        print("Invalid Path")

def main():
    print("--------Automation Script-------")

    print("Script Name :",argv[0])

    if(len(argv) !=2):
        print("Invalid Number of Arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):    #Flag for displaying help
        print("This automation script is used to perform File Automation")

    elif(argv[1]=="-u" or argv[1]=="-U"):    #Flag for displaying the usage of script
        print("Usage : Name of Script First_Argument")
        print("Example : Demo.py Marvellous Python")
        exit()

    else:
        starttime = time.time()
        DirectoryTravel(argv[1])
        endtime = time.time()

        print("Script took the time time to execute as :",endtime-starttime)

if __name__ == "__main__":
    main()
