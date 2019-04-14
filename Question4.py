import os
import sys

def DirCopyExtFile(strFilePath,strDest,strExtension):
    if(os.path.isabs(strFilePath)==False):
        strFilePath=os.path.abspath(strFilePath)
    print(strFilePath)  

    if(os.path.isdir(strFilePath)):
        destFilePath=os.getcwd()+'/'+strDest
        if(os.path.exists(destFilePath)==False):
            os.mkdir(destFilePath)
        print("reach")
        for foldername,subfolder,filename in os.walk(strFilePath):
            for file in filename:
                if(file.endswith('.'+strExtension)):
                    srcFd=open(foldername+'/'+file,'r')
                    destFd=open(destFilePath+'/'+file,'w+')
                    destFd.write(srcFd.read())
            break
    else:
        print("Invalid file path!")


def main():
    if(len(sys.argv)>3):
        try:
            DirCopyExtFile(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
        except Exception as eObj:
            print(eObj)
                
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()