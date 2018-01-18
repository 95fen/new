#八挂阵
import pyautogui
import time
from Okbtn import OKstar
from PIL.ImageOps import grayscale

print(pyautogui.getWindows())
win=pyautogui.getWindow('MNSG.exe - Build 2.05.25.0804')
print(win.get_position())
x=win.get_position()[0]
y=win.get_position()[1]
#564,63
#点击【战】按钮
def zhan():
   click_zhan= pyautogui.moveTo(x+564,y+63)
   pyautogui.click(click_zhan)
def click_btn_Act():#点击攻击按钮
    pyautogui.moveTo(x + 1085, y + 607)
    pyautogui.click(x + 1085, y + 607)
#887,329
def click_pz():
    pzbtn=pyautogui.moveTo(x+887,y+329)
    pyautogui.click(pzbtn)
#494,601
def click_ok():
    ok=pyautogui.moveTo(x+494,y+601)
    pyautogui.click(ok)


#PzBtn=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\pz.png',grayscale=True)
#pzbtn=pyautogui.locateCenterOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\pz.png',grayscale=True)
#btn=pyautogui.moveTo(pzbtn)
for i in range(20):
    click_pz()
    time.sleep(3)
    click_btn_Act()
    time.sleep(15)
    zhan()
    time.sleep(10)
    click_ok()
    time.sleep(8)
    print(i)






