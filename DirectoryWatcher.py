import sys
import os

def DirectoryWatcher(Path):
    flag=os.path.isabs(Path)
    if flag== False:
        Path=os.path.abspath(Path)
    print(Path)
    exist=os.path.isdir(Path)
    
    if exist==True:
        for foldername,subfolder,filename in os.walk(Path):
            print("Folder Names: "+foldername)
            for subf in subfolder:
                print("Sub Folder: "+subf)
            for filen in filename:
                print("File Name: "+filen)

def main():
    print("Application Name:"+sys.argv[0])
   
    if (len(sys.argv)!=2):
        print("Invalid No of Arguments")
        exit()
    if sys.argv[1]=='-h' or sys.argv[1]=='H':
        print("The script is designed for ")
        exit()
    if sys.argv[1]=='-u' or sys.argv[1]=='U':
        print("Usage: ")
        exit()
    try:
        DirectoryWatcher(sys.argv[1])

    except Exception as e:
        print("error:Invalid Input"+e)

if __name__ == "__main__":
    main()