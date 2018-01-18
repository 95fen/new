import pyautogui
import time
from PILjietudef import PilJietu
class OKstar():
    def __init__(self):
        t = PilJietu()
        okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
        while okCd == None:
            try:
                time.sleep(1)
                okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
                x2, y2 = pyautogui.center(okCd)
                btnok = pyautogui.moveTo(x2, y2)
                #t.start()#点击之前截图
                pyautogui.click(btnok)

            except:
                print(okCd)

                t.start()#截图

            continue
