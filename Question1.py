import os
import sys

def DirSearchFile(strFilePath,strExtention):
    if(os.path.isabs(strFilePath)==False):
        strFilePath=os.path.abspath(strFilePath)

    print(strFilePath)  
    if(os.path.isdir(strFilePath)):
        print("reach")
        for foldername,subfolder,filename in os.walk(strFilePath):
            for file in filename:
                if(file.endswith("."+strExtention)):
                    print(file)
            break
    else:
        print("Invalid file path!")


def main():
    if(len(sys.argv)>2):
        try:
            DirSearchFile(str(sys.argv[1]),str(sys.argv[2]))
        except Exception as eObj:
            print(eObj)
                
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()