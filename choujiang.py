import pyautogui
import time
#抽将
# def choujiang_zb():
# win= pyautogui.getWindows()
# print(win)
print(pyautogui.getWindows())#获取当前正在运行的所有程序
win = pyautogui.getWindow("MNSG.exe - Build 2.05.25.0804")#定位要操作的程序
#获取要操作程序的坐标点
print(win.get_position())
#(371, 235, 1513, 904)
x=win.get_position()[0]
y=win.get_position()[1]
num=input("请输入一个值：")
num=int(num)
z = 0
for i in range(num):

    #932,576  抽将按钮坐标
    pos1=932
    pos2=576
    pyautogui.moveTo(x + pos1, y +pos2 )
    for i in range(3):
    #pyautogui.moveTo(x + , y + 559)
        pyautogui.click(x+pos1,y+pos2)
        print(z)
        z+=1
        time.sleep(2)






