import pyautogui
import time

print(pyautogui.getWindows())
win=pyautogui.getWindow('MNSG.exe - Build 2.05.25.0804')
print(win.get_position())
x=win.get_position()[0]
y=win.get_position()[1]

# yl=pyautogui.locateOnScreen(r"C:\Users\dengxinqiang\Desktop\picture\yl.png")
# pyautogui.center(yl)
#865，477-升级
#586，544--练兵
#559，455，扣元宝
sjx=865
sjy=477
lbx=586
lby=544
kbx=559
kby=455
while x:
    pyautogui.moveTo(x+sjx,y+sjy)
    pyautogui.click(x+sjx,y+sjy)
    time.sleep(0.8)
    pyautogui.moveTo(x+lbx,y+lby)
    pyautogui.click(x+lbx,y+lby)
    time.sleep(0.8)
    pyautogui.moveTo(x+kbx,y+kby)
    pyautogui.click(x+kbx,y+kby)
    time.sleep(2)
print(3971+120)
