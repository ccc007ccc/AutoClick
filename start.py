from time import sleep
import pyautogui as pag
import random
pag.FAILSAFE = False
# 定义一个函数，用于检测是否出现了正确的提示
def check_correct():
    # 尝试在屏幕上找到correct.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen('correct.png',confidence=0.9)
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        print('Correct not found')
        # 返回False
        return False

# 定义一个函数，用于随机点击一个选项
def click_option():
    # 定义一个列表，存储所有选项的图片名
    options = ['A.png', 'A_D.png','A_DV.png', 'B.png', 'B_D.png', 'B_DV.png', 'C.png', 'C_D.png', 'C_DV.png', 'D.png', 'D_D.png', 'D_DV.png']
    # 从列表中随机选择一个图片名
    option = random.choice(options)
    # 尝试在屏幕上找到该图片的位置
    try:
        x, y = pag.locateCenterOnScreen(option,region=(616, 325, 1250, 810),grayscale=True,confidence=0.9)
        # 如果找到了，移动鼠标到该位置，并点击一次
        pag.moveTo(x, y)
        pag.click()
        pag.moveTo(0, 0)
    # 如果没有找到，抛出异常
    except TypeError:
        # 打印错误信息，并继续执行
        print('未找到选项')

# 定义一个函数，用于点击关闭按钮
def click_close():
    # 尝试在屏幕上找到close.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen('close.png')
        # 如果找到了，移动鼠标到该位置，并点击一次
        pag.moveTo(x, y)
        pag.click()
        sleep(0.7)
        pag.click()
    # 如果没有找到，抛出异常
    except TypeError:
        # 打印错误信息，并继续执行
        print('Close button not found')

# 定义一个循环，用于不断重复以下步骤：
while True:
    # 调用检测正确提示的函数，如果找到了，就调用点击关闭按钮的函数，并结束循环
    if check_correct():
        click_close()
    # 如果没有找到正确提示，就调用随机点击选项的函数
    else:
        click_option()
