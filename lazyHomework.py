import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


#These are the path hich you need to change or you may have to create new folder

paths = {
        'math':'/home/kanishk/Desktop/Learn/ha', 
        'phy':'/home/kanishk/Desktop/Learn/ha',
        'chem': '/home/kanishk/Desktop/Learn/ha',
        'bio': '/home/kanishk/Desktop/Learn/ha',
        'cs':'/home/kanishk/Desktop/Learn/ha',
        'comp':'/home/kanishk/Desktop/Learn/ha',
        'sst':'/home/kanishk/Desktop/Learn/ha',
        'other':'/home/kanishk/Desktop/Learn/ha',
        }

def homework(filename):
    try:
        file = filename.replace('_',' ') 
    except Exception as e:
        print('Error was: ',e)
        file = filename.replace('-',' ')
    if 'math' in file:
        placer(file,'Key','Notes','math')
    elif 'phy' in file:
        placer(file,'question*','notes',"phy")
    elif 'Chem' in file:
        placer(file,'HW','notes','chem')
    elif 'bio' in file:
        placer(file,'hw','notes','bio')
    elif 'CS' in file:
        placer(file,'Homework','Notes','cs')
    # Thes may be wrong becase i didn't have same name for file 
    elif 'comp' in file:
        placer(file,'Homework','N*',"comp")
    elif 'His' in file:
        placer(file,'Homework','Notes','sst')
    else: 
        os.chdir(paths['other'])
def placer(file,hw,notes,key):
    if hw in file or 'Hw' in file:
        
        os.chdir(f"{paths[key]}/homework")
    elif notes in file:
        os.chdir(f"{paths[key]}/Notes")
    else:
        os.chdir(f"{paths[key]}/other")

def cuter(filename):
    print(f"file was selected for cuting is {filename}")
    srcFile = os.getcwd()
    with open(filename,'rb') as f:
        data = f.read()
    homework(filename)
    with open(filename,'wb') as f:
        f.write(data)
    os.chdir(srcFile)
    os.remove(filename)


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        os.chdir(f"{direction}/kan")  
        files = os.listdir()
        modefitedList = list(set(files).difference(set(startingFile)))
        for file in modefitedList:
            cuter(file)    
        os.chdir(direction) 

direction = os.getcwd()
os.chdir(f"{direction}/kan")  
startingFile = os.listdir()
os.chdir(direction) 

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='kan', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
