import pyautogui

while 1:
    print(pyautogui.position())
    data = input('Hit get again and q to exit: ')
    if data == 'q':
        break
