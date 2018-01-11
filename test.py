import pyautogui
import time



print(pyautogui.getWindows())
win = pyautogui.getWindow("MNSG_trunk.exe - Build 2.05.25.0804")
x=win.get_position()[0]
y=win.get_position()[1]


def aa():
    try:
        import Image
    except ImportError:
        from PIL import ImageGrab

    i = 1
    while i <= 1:
        im = ImageGrab.grab(win.get_position())
        im.save(r'C:\Users\dengxinqiang\Desktop\picture\错误截图\a'+str(i) + ".jpg")
        print("screen...")
        time.sleep(10)
        i = i + 1


try:
    for i in range(1,100):
        pyautogui.moveTo(x+882,y+333)
        pyautogui.click(x+882,y+333)
        time.sleep(2)
        pyautogui.moveTo(x+1079,y+607)
        pyautogui.click(x+1079,y+607)
        okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
        while okCd == None:
            try:
                time.sleep(10)
                okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
                x2, y2 = pyautogui.center(okCd)
                btnok = pyautogui.moveTo(x2, y2)
                pyautogui.click(btnok)

            except:
                print(okCd)
                aa()
        continue
except:
    print("出错误了")






#1079,607
#484,612
