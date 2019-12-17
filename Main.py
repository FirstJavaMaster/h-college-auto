import pyautogui

from ClickHelper import ClickHelper
from challenge.Challenge import Challenge


def main():
    print('采集基本信息...')

    screen_size = pyautogui.size()
    print('屏幕大小: %s - %s' % (screen_size.width, screen_size.height))

    origin = ClickHelper.get_origin()
    print('游戏窗口起点 x:%d y:%d' % (origin.x, origin.y))


if __name__ == '__main__':
    main()

    Challenge.run()
