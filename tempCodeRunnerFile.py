def check_correct():
    # 尝试在屏幕上找到correct.png图片的位置
    try:
        x, y = pag.locateCenterOnScreen('correct.png')
        # 如果找到了，返回True
        return True
    # 如果没有找到，抛出异常
    except TypeError:
        print('Correct not found')
        # 返回False
        return False
