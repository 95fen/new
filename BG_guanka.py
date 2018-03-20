import time
import pyautogui


#《小小军团合战三国PC》.exe
#win=pyautogui.getWindow('MNSG.exe') #测试PC
win=pyautogui.getWindow('《小小军团合战三国PC》.exe')  #报审
print(win.get_position())
x=win.get_position()[0]
y=win.get_position()[1]
i=1;
#破阵按钮886，333
# 战按钮1082,610
#结束快捷键563，64
#确定按钮477，603
#体力按钮728,399

tlx=x+728
tly=y+399
zx=x+1082
zy=y+610
jsx=x+563
jsy=y+64
okx=477+x
oky=603+y
stop=0;
while stop<50:
     pyautogui.moveTo(x+886,y+333);
     pyautogui.click(x+886,y+333);
     time.sleep(5)
     if(stop%4==0):
         pyautogui.moveTo(zx,zy)
         pyautogui.click(zx,zy)
         time.sleep(3)
         pyautogui.moveTo(tlx, tly)
         pyautogui.click(tlx, tly)
     else:
          pyautogui.moveTo(zx, zy)
          pyautogui.click(zx, zy)

     time.sleep(15)
     pyautogui.click(jsx,jsy)
     time.sleep(6)
     pyautogui.click(okx,oky)
     time.sleep(6)
     stop+=1
     print("第",stop,"次")


