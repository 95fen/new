import pyautogui
import PIL
import time
import datetime
try:
    import Image
except ImportError:
    from PIL import ImageGrab
from PIL import ImageGrab


class PilJietu(object):
    def start(self):
        win = pyautogui.getWindow("MNSG.exe - Build 2.05.25.0804")
        i = 1

        time_str = time.strftime('%d%H%M%S', time.localtime())

        print(time_str)
        while i <= 1:
            im = ImageGrab.grab(win.get_position())
            im.save(r'C:\Users\dengxinqiang\Desktop\picture\错误截图\a' + str(i) + time_str + ".jpg")
            print("screen...")
            time.sleep(10)
            i = i + 1


x = PilJietu()
x.start()
