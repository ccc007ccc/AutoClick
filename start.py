# 导入PyQt5和PyAutoGUI库
from PyQt5.QtWidgets import QApplication
import pyautogui


# 定义一个标志变量，表示是否找到button.png
found = False

while True:
    # 循环直到找到button.png
    while not found:

        # 从屏幕中找到button.png的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen('button.png')


        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)

            # 点击中心点坐标
            pyautogui.click(x, y)

            # 设置标志变量为True，表示找到了button.png
            found = True
            print('找到button.png')
        
        if not found:
            print('没有找到button.png')
    #是否继续
    choice = input('是否继续？(y/n)')
    if choice == 'y':
        found = False
    else:
        break

