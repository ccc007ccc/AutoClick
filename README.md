# AutoClick

基于 pyautogui 的自动点击

## 使用教程

1. 安装 [Python 3](https://www.python.org/downloads/)
2. 安装 PyQt5 和 pyautogui：`pip install PyQt5 pyautogui opencv-python keyboard`
3. 运行 `python start.py`

## 注意事项


1. 请不要在使用过程中移动鼠标。
2. 如果运行后没有动静，请把 `start.py` 中 `x, y = pag.locateCenterOnScreen(option,region=(616, 325, 1250, 810),grayscale=True,confidence=0.9)` 的 `region` 参数删除。
3. 自动寻找下一题的功能暂时因为缺少图片而无法点击大于第二题的选项。如果您有图片，请在 issue 中提交，谢谢。
4. 此程序是在 1080p Edge 浏览器最大化的Python 3.11环境下测试的。如果您的环境不同，请自行修改 `start.py` 中的参数。
5. 目前经过测试发现很多电脑不能成功识别到图像，如果碰到这个问题请手动替换屏幕截图文件。
