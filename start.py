# 导入PyQt5和PyAutoGUI库
from PyQt5.QtWidgets import QApplication
import pyautogui

import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    #在这里写你的程序代码
    

    exit = False

    # 定义一个标志变量，表示是否找到button.png
    steam_found = False
    steam = 'img/steam.png'
    steam_y = False

    game_found = False
    game = 'img/game.png'
    game_y = False



    def bug():
        Skill1()
        Skill2()
        Skill3()
        Skill4()
        gameL()
        login()

    def Skill4():
        kill4 = 'img/kill4.png'
        # 从屏幕中找到kill1的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(kill4)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + kill4)

    def Skill3():
        no = 'img/no.png'
        # 从屏幕中找到no的位置，返回一个(x, y, width, height)的元组  
        region = pyautogui.locateOnScreen(no)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + no)

    def login():
        windowS = 'img/windowS.png'
        password = 'img/password.png'
        login = 'img/login.png'
        passJ = 'img/passJ.png'
        # 从屏幕中找到windowS的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(windowS)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + windowS)

        # 从屏幕中找到password的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(password)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            pyautogui.typewrite('StarWarsLeroy4ikk_',interval=0.3)
            print('找到' + password)
        
        # 从屏幕中找到passJ的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(passJ)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + passJ)
        
        # 从屏幕中找到login的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(login)
        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)
            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + login)



    def Skill1():
        kill1 = 'img/kill1.png'
        # 从屏幕中找到kill1的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(kill1)

        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)

            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + kill1)

    def Skill2():
        kill2 = 'img/kill2.png'
        # 从屏幕中找到kill1的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(kill2)

        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)

            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)
            print('找到' + kill2)

    # Steam
    def steam_play():
        play_y = False
        play = 'img/play.png'
        kill = 'img/kill.png'
        # 从屏幕中找到steam的位置，返回一个(x, y, width, height)的元组
        region = pyautogui.locateOnScreen(steam)

        # 如果找到了，就获取中心点坐标
        if region:
            x, y = pyautogui.center(region)

            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)

            # 设置标志变量为True，表示找到了
            global steam_y
            steam_y = True
            print('找到' + steam)
            
            bug()

            while play_y == False:
                # 从屏幕中找到play的位置，返回一个(x, y, width, height)的元组
                pyautogui.sleep(1)
                region = pyautogui.locateOnScreen(play)
                region = pyautogui.locateOnScreen(play)

                # 如果找到了，就获取中心点坐标
                if region:
                    x, y = pyautogui.center(region)

                    # 点击中心点坐标
                    pyautogui.click(x, y,duration=0.4)

                    bug()

                    # 设置标志变量为True，表示找到了
                    play_y = True
                    print('找到' + play)
                else:
                    print('没有找到'+ play)
                    #循环重新找steam并点击,直到找到play
                    while True:
                        #暂停一秒
                        pyautogui.sleep(1)
                        # 从屏幕中找到steam的位置，返回一个(x, y, width, height)的元组
                        region = pyautogui.locateOnScreen(steam)

                        # 如果找到了，就获取中心点坐标
                        if region:
                            x, y = pyautogui.center(region)

                            # 点击中心点坐标
                            pyautogui.click(x, y,duration=0.4)

                            bug()

                            print('找到' + steam)
                            break
                        else:
                            print('没有找到'+ steam)
            
            #检查三秒是否有kill,有就点击,没有就继续
            pyautogui.sleep(3)
            region = pyautogui.locateOnScreen(kill)
            if region:
                x, y = pyautogui.center(region)
                pyautogui.click(x, y,duration=0.4)
                print('找到' + kill)

        else:
            print('没有找到'+ steam)

    def gameL():
        done_y = False
        done = 'img/done.png'
        # 从屏幕中找到game的位置，返回一个(x, y, width, height)的元组
        regionG = pyautogui.locateOnScreen(game)

        # 如果找到了，就获取中心点坐标
        if regionG:
            x, y = pyautogui.center(regionG)

            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)

            # 设置标志变量为True，表示找到了
            global game_y
            game_y = True
            print('找到' + game)

            # 从屏幕中找到done的位置，返回一个(x, y, width, height)的元组
            region = pyautogui.locateOnScreen(done)

            # 如果找到了，就获取中心点坐标
            if region:
                x, y = pyautogui.center(region)

                # 点击中心点坐标
                pyautogui.click(x, y,duration=0.4)

                # 设置标志变量为True，表示找到了
                done_y = True
                print('找到' + done)
            else:
                print('没有找到'+ done)
        #循环重新找game并点击,直到找到done
                # 从屏幕中找到game的位置，返回一个(x, y, width, height)的元组
                regionG = pyautogui.locateOnScreen(game)

                # 如果找到了，就获取中心点坐标
                if regionG:
                    x, y = pyautogui.center(regionG)

                    # 点击中心点坐标
                    pyautogui.click(x, y,duration=0.4)
                    print('找到' + game)
                else:
                    print('没有找到'+ game)
                                
        else:
            print('没有找到'+ game)

    # Game
    def gameC():
        done_y = False
        done = 'img/done.png'
        # 从屏幕中找到game的位置，返回一个(x, y, width, height)的元组
        regionG = pyautogui.locateOnScreen(game)

        # 如果找到了，就获取中心点坐标
        if regionG:
            x, y = pyautogui.center(regionG)

            # 点击中心点坐标
            pyautogui.click(x, y,duration=0.4)

            # 设置标志变量为True，表示找到了
            global game_y
            game_y = True
            print('找到' + game)

            while done_y == False:
                # 从屏幕中找到done的位置，返回一个(x, y, width, height)的元组
                region = pyautogui.locateOnScreen(done)

                # 如果找到了，就获取中心点坐标
                if region:
                    x, y = pyautogui.center(region)

                    # 点击中心点坐标
                    pyautogui.click(x, y,duration=0.4)

                    # 设置标志变量为True，表示找到了
                    done_y = True
                    print('找到' + done)
                else:
                    print('没有找到'+ done)
                    #循环重新找game并点击,直到找到done
                    while True:
                        # 从屏幕中找到game的位置，返回一个(x, y, width, height)的元组
                        regionG = pyautogui.locateOnScreen(game)

                        # 如果找到了，就获取中心点坐标
                        if regionG:
                            x, y = pyautogui.center(regionG)

                            # 点击中心点坐标
                            pyautogui.click(x, y,duration=0.4)
                            print('找到' + game)
                            break
                        else:
                            print('没有找到'+ game)
                                
        else:
            print('没有找到'+ game)



    while exit == False:
        # 循环直到找到
        while True:
            # 调用steam_play()函数
            steam_play()

            # 如果找到了，就设置标志变量为True，结束循环
            if steam_y == True:
                break
        
        while True:
            # 调用gameC()函数
            gameC()

            # 如果找到了，就设置标志变量为True，结束循环
            if game_y == True:
                break

        #是否继续
        # choice = input('是否继续？(y/n)')
        # if choice == 'y':
        #     steam_found = False
        # else:
        #     exit = True
        #     break
        

else:
    #以管理员身份重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

