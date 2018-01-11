import pyautogui
import time
time.sleep(0.5)
#print(pyautogui.position())
# pyautogui.moveTo(247,766)#移动位置
# pyautogui.click(247,766)
# pyautogui.typewrite('hello',0.25)
# time.sleep(1)#等待时间
# pyautogui.click(846,810)
#
# pyautogui.alert('aa','bb','ok')

buttonbq=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\2\表情测试.png')
print(buttonbq)
x,y=pyautogui.center(buttonbq)
pyautogui.moveTo(x,y)
pyautogui.click(x,y)
time.sleep(1)
buttonbq2=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\2\test2.png')
x1,y1=pyautogui.center(buttonbq2)
pyautogui.moveTo(x1,y1)
pyautogui.click(x1,y1)
time.sleep(1)
buttonfs=pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\2\fs.png')
x2,y2=pyautogui.center(buttonfs)
pyautogui.moveTo(x2,y2)
pyautogui.click(x2,y2)