import os
import moviepy.editor as mp

Direction = os.getcwd()
try:
    os.makedirs('Modifier')

except FileExistsError:
    pass

Path = '\Modifier'
DirectionPath = Direction+Path
os.chdir(DirectionPath)
Files = os.listdir()
Extensions = ['mp4']
for File in Files:
    FileName = File.split('.')
    FileLength = len(FileName)
    FileLength -= 1
    if FileLength != 0:
        Extension = FileName[FileLength]
        if Extension in Extensions:
            DirExtension = '\mp3'

            try:
                os.makedirs('mp3')

            except FileExistsError:
                pass

        else:
            continue
    else:
        print("File Skipped ", File)
        continue

    filename = FileName[0]
    filename = f"{filename}.{'mp3'}"
    if Extension in Extensions:
        Video = mp.VideoFileClip(File)
        os.chdir(DirectionPath + DirExtension)
        Video.audio.write_audiofile(filename)
        os.chdir(DirectionPath)
        print("Converted successful")
