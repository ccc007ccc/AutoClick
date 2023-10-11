from time import sleep
import pyautogui as pag
import random
import os
import keyboard

pag.FAILSAFE = False

# 检测多选
def check_multiple():
    # 尝试在屏幕上找到多选题的图片位置
    try:
        x, y = pag.locateCenterOnScreen("multiple.png", confidence=0.91)
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False


# 定义一个函数，用于检测是否出现了正确的提示
def check_correct():
    # 尝试在屏幕上找到correct.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen("correct.png", confidence=0.9)
        # 输出绿色字
        print("\033[0;32m" + "找到正确提示" + "\033[0m")
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False

def check_error():
    # 尝试在屏幕上找到error.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen("error.png", confidence=0.98)
        # 输出红色字
        print("\033[0;31m" + "找到错误提示" + "\033[0m")
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False
    
#检测视频进度条
def check_progress():
    # 尝试在屏幕上找到progress.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen("progress.png", confidence=0.95)
        # 输出黄色字
        print("\033[0;33m" + "找到视频进度条" + "\033[0m")
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False
    
#点击视频下个视频按钮
def check_nextV():
    # 尝试在屏幕上找到next.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen("nextV.png", confidence=0.95)
        # 输出黄色字
        print("\033[0;33m" + "找到下个视频按钮" + "\033[0m")
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False

#左右滑动鼠标触发视频进度条
def move_mouseV():
    # 鼠标左右滑动
    pag.moveTo(460, 540)
    print("\033[0;33m" + "滑动鼠标" + "\033[0m")

#检查视频是否播放完毕
def check_end():
    #截图对比下一帧
    end = pag.screenshot()
    try:
        x, y = pag.locateCenterOnScreen(end, confidence=0.99)
        # 输出黄色字
        print("\033[0;33m" + "视频已结束" + "\033[0m")
        pag.moveTo(x, y)
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 返回False
        return False

#移动鼠标->检查视频进度条->点击下个视频按钮
def click_nextV():
    if check_end():
        move_mouseV()
        if check_progress():
            if check_nextV():
                pag.click()
                sleep(4)
                pag.moveTo(460, 540)
                pag.click()
                pag.moveTo(0, 0)
                return True
            else:
                print("\033[0;33m" + "未找到下个视频按钮" + "\033[0m")
                pag.moveTo(0, 0)
                return False
    else:
        return False

# 定义一个函数，传入选项的图片名，用于点击选项
def click_option(option, number):
    # 尝试在屏幕上找到该图片的位置
    try:
        x, y = pag.locateCenterOnScreen(
            option, region=(616, 325, 1250, 810), confidence=number
        )
        # 输出黄色字
        print("\033[0;33m" + "找到选项" + option + "\033[0m")
        # 如果找到了，移动鼠标到该位置，并点击一次
        pag.moveTo(x, y)
        pag.click()
        pag.moveTo(0, 0)

        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 打印错误信息，并继续执行
        print("未找到选项" + option)
        return False
    except OSError:
        # 打印错误信息，并继续执行
        print("无法读取 " + option + "，因为文件丢失、权限不正确或格式不受支持或无效")
        return False
    


# 定义一个函数，用于点击关闭按钮
def click_close():
    # 尝试在屏幕上找到close.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen("close.png", confidence=0.9)
        # 如果找到了，移动鼠标到该位置，并点击一次
        pag.moveTo(x, y)
        pag.click()
        sleep(0.7)
        pag.click()
    # 如果没有找到，抛出异常
    except TypeError:
        # 打印错误信息，并继续执行
        print("Close button not found")


# 定义一个函数，用于点击后面的题目
def click_next(int):  # 传入循环次数
    # 尝试在屏幕上找到循环次数.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen(str(int) + ".png")
        # 如果找到了，移动鼠标到该位置，并点击一次
        pag.moveTo(x, y)
        pag.click()

        return True
    # 如果没有找到，抛出异常
    except TypeError:
        # 打印错误信息，并继续执行
        print("未找到下一题按钮")
        return False
    except OSError:
        # 打印错误信息，并继续执行
        print("无法读取 " + str(int) + ".png，因为文件丢失、权限不正确或格式不受支持或无效")
        return False



#是否打开自动播放下个视频
inputV = input("是否打开自动播放下个视频？(y/n)")
if inputV == 'y':
    autoNextV = True
else:
    autoNextV = False

def continue_run():
    # 定义一个循环，用于不断重复以下步骤：
    i = 1

    # 单选图片为x.png，多选图片为x_D.png，多选选中为x_DV.png
    # 定义一个列表，存储所有选项的图片名

    optionList = ['A','B','C','D','E']
    options = []
    for letter in optionList:
        options.append(letter + '.png')
        options.append(letter + '_D.png')
        options.append(letter + '_DV.png')

    # 定义单选列表，存储所有选项的图片名
    singleOptions = []
    for letter in optionList:
        singleOptions.append(letter + '.png')

    # 定义多选列表，存储所有选项的图片名
    multipleOptions = []
    for letter in optionList:
        multipleOptions.append(letter + '_D.png')


    # 定义一个列表，存储所有错误提示的图片名
    errorOptions = []
    correctOptions = []
    while True:
        #检查是否打开自动播放下个视频
        if autoNextV:
            click_nextV()
        else:
            print("\033[0;33m" + "未打开自动播放下个视频" + "\033[0m")
        #检查是否是多选题
        if check_multiple():
            options = multipleOptions
        else:
            options = singleOptions
        # 调用检测正确提示的函数，如果找到了，就调用点击关闭按钮的函数，并结束循环
        if check_correct():
            errorOptions = []
            correctOptions = []
            i += 1
            # 检查有没有下一题
            if click_next(i):
                continue
            else:
                click_close()
                i = 1
        # 如果没有找到正确提示，就调用随机点击选项的函数
        else:
            # 在options中减去错误选项和正确选项
            options = list(set(options) - set(errorOptions) - set(correctOptions))
            print(options)
            # 从列表中随机选择一个图片名
            option = random.choice(options)        
            print(option)
            if click_option(option, 0.9):
                # 检测错误提示
                if check_error():
                    if check_multiple():
                        #获取首字母
                        letter = option[0]
                        errorOptions.append(letter + '_D.png')
                        errorOptions.append(letter + '_DV.png')
                        #重复点击已选中的错误选项直到错误提示消失
                        while check_error():
                            if click_option(letter + '_DV.png',0.98):
                                continue
                            else:
                                print("未找到选项" + letter + '_DV.png')
                    else:
                        #获取首字母
                        letter = option[0]
                        errorOptions.append(letter + '.png')
                    
                else:
                    #获取首字母
                    letter = option[0]
                    correctOptions.append(letter + '.png')
                    correctOptions.append(letter + '_D.png')
                    correctOptions.append(letter + '_DV.png')
    





print("\033[0;33m" + "请将鼠标移动到视频播放区域,按ctrl+alt+s开始运行" + "\033[0m")
keyboard.add_hotkey('ctrl+alt+s', continue_run) 

keyboard.wait()

