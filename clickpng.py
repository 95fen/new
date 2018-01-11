import pyautogui
import time

from PIL.ImageOps import grayscale

i=1
while i==1:
    pzCd=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\pz.png',grayscale=True)
    x,y=pyautogui.center(pzCd)
    btn=pyautogui.moveTo(x,y)
    pyautogui.click(btn)
    time.sleep(2)
    gjCd=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\gj.png',grayscale=True)
    x1,y1=pyautogui.center(gjCd)
    btngj=pyautogui.moveTo(x1,y1)
    pyautogui.click(btngj)
   # time.sleep(120)


    okCd=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
    while okCd == None:
        try:
            time.sleep(10)
            okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
            x2, y2 = pyautogui.center(okCd)
            btnok = pyautogui.moveTo(x2, y2)
            pyautogui.click(btnok)

        except:
            print(okCd)
    time.sleep(5)
    print(pzCd)

#pyautogui.center()


