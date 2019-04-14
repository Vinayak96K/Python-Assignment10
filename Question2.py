import os
import sys

def DirRenameFile(strFilePath,strExtention1,strExtention2):
    if(os.path.isabs(strFilePath)==False):
        strFilePath=os.path.abspath(strFilePath)

    print(strFilePath)  
    if(os.path.isdir(strFilePath)):
        print("reach")
        for foldername,subfolder,filename in os.walk(strFilePath):
            for file in filename:
                if(file.endswith("."+strExtention1)):
                    Temp=str(file)
                    Temp=file.replace(strExtention1,strExtention2)
                    print(strExtention2)
                    print(file)
                    print(Temp)
                    os.rename(foldername+'/'+file,foldername+'/'+Temp)
            break
    else:
        print("Invalid file path!")


def main():
    if(len(sys.argv)>3):
        try:
            DirRenameFile(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
        except Exception as eObj:
            print(eObj)
                
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()