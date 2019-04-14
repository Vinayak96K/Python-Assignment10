import os
import sys

def DirCopyFile(strFilePath,strDest):
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
                srcFd=open(foldername+'/'+file,'r')
                destFd=open(destFilePath+'/'+file,'w+')
                destFd.write(srcFd.read())
            break
    else:
        print("Invalid file path!")


def main():
    if(len(sys.argv)>2):
        try:
            DirCopyFile(str(sys.argv[1]),str(sys.argv[2]))
        except Exception as eObj:
            print(eObj)
                
    else:
        print("Incorrect arguments!")

if __name__ == "__main__":
    main()