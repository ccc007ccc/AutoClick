
# AutoClick

    基于pyautogui的自动点击

# 使用教程

1. 安装[python3](https://www.python.org/downloads/)
2. 安装pyqt5和pyautogui: `pip install PyQt5 pyautogui`
3. 运行`python start.py`

# 注意事项

1. 请不要在使用过程中移动鼠标
2. 如果运行后没有动静请把start.py中`x, y = pag.locateCenterOnScreen(option,region=(616, 325, 1250, 810),grayscale=True,confidence=0.9)`的region参数删除.
3. 自动寻找下一题的功能暂时因为缺少图片而无法点击大于第二题的选项,如果你有图片请在issue中提交,谢谢.
