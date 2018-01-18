import pyautogui
import time
import PIL
from PILjietudef import PilJietu
from Okbtn import OKstar
#掠夺战功能
win=pyautogui.getWindow("MNSG.exe - Build 2.05.25.0804")
x=win.get_position()[0]#获取窗口的X坐标
y=win.get_position()[1]#获取窗口的Y坐标
jietu = PilJietu()  # 初始化截图对象
def click_btn_tili():#点击补充体力按钮
    pyautogui.moveTo(x + 736, y + 401)
    pyautogui.click(x + 736, y + 401)
   # time.sleep(1.5)
    # 736,401 购买体力
def click_btn_Act():#点击攻击按钮
    pyautogui.moveTo(x + 1085, y + 607)
    pyautogui.click(x + 1085, y + 607)
    #time.sleep(1.5)
    # 1085,607
def click_btn_ss():#点击搜索按钮
    time.sleep(0.5)
    pyautogui.moveTo(x + 564, y + 491)
    pyautogui.click(x + 564, y + 491)
    # 564,491

i=1
while i==1:
    jietu.start()  # 点击前截图
    time.sleep(0.5)
   # okCd = pyautogui.locateOnScreen(r'C:\Users\dengxinqiang\Desktop\picture\ok.png', grayscale=True)
    click_btn_Act()
    time.sleep(3)
    click_btn_tili()
    time.sleep(2)
    click_btn_Act()
    time.sleep(3)
    OKstar()
    time.sleep(5)
    click_btn_ss()
    time.sleep(5)
    jietu.start()
