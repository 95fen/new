import time
import pyautogui

#破阵按钮886，333
# 战役参战按钮899,666
# 战按钮1082,610
#结束快捷键563，64
#确定按钮477，603
#体力按钮728,399
win=pyautogui.getWindow('《小小军团合战三国PC》.exe')
print(win.get_position())
x=win.get_position()[0]
y=win.get_position()[1]
i=1;
tlx=x+728
tly=y+399
zx=x+971
zy=y+742
jsx=x+507
jsy=y+65
okx=417+x
oky=672+y
czx=x+673;
czy=y+466;
stop=0;
while stop<100:
    # pyautogui.click(czx, czy)
     #time.sleep(2)
     pyautogui.moveTo(x+899,y+666);
     for index in range(1,3):
        pyautogui.click(x+899,y+666);
        time.sleep(1)
     time.sleep(5)
     if(stop%6==0):
         pyautogui.moveTo(zx,zy)
         for index in range(1,6):
             pyautogui.click(zx,zy)
             time.sleep(1)
         time.sleep(7)
        # pyautogui.moveTo(tlx, tly)
         #pyautogui.click(tlx, tly)
     else:
          pyautogui.moveTo(zx, zy)
          for index in range(1, 6):
              pyautogui.click(zx, zy)
              time.sleep(1)

     time.sleep(8)
     pyautogui.click(jsx,jsy)
     time.sleep(8)
     pyautogui.click(okx,oky)
     time.sleep(6)
     #pyautogui.click(czx,czy)
     #time.sleep(2)
    # pyautogui.click(x+155,y+667)
     #time.sleep(3)
     stop+=1
     print("第",stop,"次")