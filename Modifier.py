import os
from datetime import datetime
import array as arr

def listToString(s):  
    str1 = " "    
    for ele in s:  
        str1 += ele      
    return str1 

def FileWriter(UserFile,TobeFeed):
    with open(UserFile,"wb") as bwriter:
        bwriter.write(TobeFeed)

def ExtensionFinder(FileName):
    FileName = FileName.split(".")
    a = len(FileName)
    a -=1
    Name = FileName[0]
    Extension = FileName[a]
    print("File copied to ",Extension)
    return Name,Extension
def Deletdir(value,filepath,filename):
    os.chdir(Direction)
    if value == True:
        filepath
        print("Deleted")
        os.remove(filename)

def FileCreater(Name):
    try:
        with open(Name,"w") as created:
            pass
    except PermissionError:
        print("It was there")
        pass

Direction = os.getcwd()
Path = '\ModifiedFiles'
Extensions = []
DeletFile = False
print(Direction)
try:
    os.chdir(Direction)
    os.mkdir('ModifiedFiles')

except:
    pass

print("It will modify of this location ",Direction)
if __name__ == "__main__":
    os.chdir(Direction)
    choice = int(input("You Choice: "))
    if choice == 1:
        Files = os.listdir()
        os.chdir(Direction+Path)
        UserChoice = input("You Want to Delet file?\nA.Yes\nB.No\nChoice: ")
        UserChoice = UserChoice.lower()
        if UserChoice == 'a':
            DeletFile = True

        elif UserChoice == 'b':
            print("Ok file will remain there....")
            pass
        else:
            print("Invailied Choice \n file will remain there.")
            
        for File in Files:
            os.chdir(Direction)
            if File != "Modifyer.py":
                try:
                    breader = open(File,"rb")
                    data = breader.read()
                    breader.close()
                    
                    try:
                        os.chdir(Direction+Path+'\Finaly')
                    except FileNotFoundError:
                        os.chdir(Direction+Path)
                        os.mkdir('Finaly')
                        os.chdir(Direction+Path+'\Finaly')

                    Extensionsdirs = os.listdir()
                    for  Extensionsdir in Extensionsdirs:
                        Extensions.append(Extensionsdir)
                        
                        os.chdir(Direction+Path)
                    

                    try:
                        Extension = ExtensionFinder(File)[1]

                    except IndexError:
                        continue

                    else:
                        FileExtension = "\{}".format(Extension)
                        
                        if Extension not in Extensions:
                            os.chdir(Direction+Path+'\Finaly')
                            os.makedirs(Extension)
                            Extensions.append(Extension)
                            print("File Created")
                            try:
                                os.chdir(Direction+Path+'\Finaly'+FileExtension)
                                FileWriter(File,data)
                                Deletdir(DeletFile,os.chdir(Direction+Path),File)
                            except FileNotFoundError:
                                continue

                        else:  
                            try:
                                os.chdir(Direction+Path+'\Finaly'+FileExtension)
                                FileWriter(File,data)
                                Deletdir(DeletFile,os.chdir(Direction+Path),File)
                            except FileNotFoundError:
                                continue

                except PermissionError:
                    continue
            else:
                continue      
    elif choice == 2:   
        os.chdir(Direction+Path)
        Videos = os.listdir()
        DeletFile = False
        UserChoice = input("You Want to Delet file?\nA.Yes\nB.No\nChoice: ")
        UserChoice = UserChoice.lower()
        if UserChoice == "a":
            DeletFile = True
        else:
            pass
        try:
            os.makedirs("Artist")
        except:
            pass       
        for Video in Videos:
            Video_splited = Video.split(" - ")
            Artist = Video_splited[0]
            os.chdir(Direction+Path)
            try:
                with open(Video,"rb") as breader:
                    Data = breader.read()
            except PermissionError:
                continue
            try:
                Name = Video_splited[1]
            except IndexError:
                continue          
            os.chdir(Direction+Path+"\Artist")
            File = os.listdir()
            Artistdir = "\{}".format(Artist)
            if Artist not in File:
                File.append(Artist) 
                os.makedirs(Artist)
                os.chdir(Direction+Path+"\Artist"+Artistdir)

            else:
                os.chdir(Direction+Path+"\Artist"+Artistdir)
            FileCreater(Video)
            FileWriter(Video,Data)
            print(Video," Copied in ",Artist)

            if DeletFile == True:
                os.chdir(Direction+Path)
                os.remove(Video)
                print(Video," Removed")
            else:
                continue