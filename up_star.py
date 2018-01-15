import pyautogui
import time


print(pyautogui.getWindows())
win=pyautogui.getWindow('MNSG.exe - Build 2.05.25.0804')
print(win.get_position())
x=win.get_position()[0]
y=win.get_position()[1]




#643,53  升星按钮
sxax=643
sxay=53
#714，605 二级升星菜单
sxbx=714
sxby=605
#579，478  扣元宝按钮
kx=579
ky=478
#690,620下一个武将
nexx=690
nexy=620
stop=0
while stop<=50:
    for i in range(8):
        pyautogui.moveTo(x+sxax,y+sxay)
        pyautogui.click(x+sxax,y+sxay)
        time.sleep(1)
        pyautogui.moveTo(x+sxbx,y+sxby)
        pyautogui.click(x+sxbx,y+sxby)
        time.sleep(1)
        pyautogui.moveTo(x+kx,y+ky)
        pyautogui.click(x+kx,y+ky)
        time.sleep(1)
        pyautogui.moveTo(x+kx,y+ky)
        pyautogui.click(x+kx,y+ky)
        time.sleep(2)
    pyautogui.moveTo(x+nexx,y+nexy)
    pyautogui.click(x+nexx,y+nexy)
    time.sleep(3)
    stop+=1
    print("已执行:",stop,"次")



