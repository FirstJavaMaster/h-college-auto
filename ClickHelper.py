import time

import pyautogui


class ClickHelper:
    # 游戏窗口的起点
    @staticmethod
    def get_origin():
        pos = pyautogui.locateCenterOnScreen('src/app.png')
        if pos is None:
            raise RuntimeError('未找到游戏窗口, 请将游戏窗口放置在屏幕前端')
        # 调整坐标, 使其定位到左上角的起点. 偏移量是图片长宽的一半
        return pyautogui.position(pos.x - 90, pos.y - 15)

    # 根据偏移量计算出绝对坐标
    @staticmethod
    def __get_absolutely_position__(offset_x, offset_y):
        origin = ClickHelper.get_origin()
        return pyautogui.position(origin.x + offset_x, origin.y + offset_y)

    @staticmethod
    def click(offset_x, offset_y, wait_second=0.5):
        raw_pos = pyautogui.position()
        pyautogui.click(ClickHelper.__get_absolutely_position__(offset_x, offset_y))
        pyautogui.moveTo(raw_pos)
        time.sleep(wait_second)

    @staticmethod
    def click_pic(pic_path, already_pic_path=None, wait_second=0.5, confidence=0.9):
        if pic_path is None:
            raise RuntimeError('请传入图片路径')

        pos = pyautogui.locateCenterOnScreen(pic_path, confidence=confidence)
        if pos is None:
            if already_pic_path is None:
                raise RuntimeError("无法定位到 " + pic_path)
            else:
                exist = ClickHelper.exist(already_pic_path)
                if exist:
                    print('已处于 ' + already_pic_path)
                else:
                    raise RuntimeError("无法定位到(替补) " + already_pic_path)
        else:
            raw_pos = pyautogui.position()
            pyautogui.click(pos)
            pyautogui.moveTo(raw_pos)
            time.sleep(wait_second)

    @staticmethod
    def scroll(offset_x, offset_y, clicks, wait_second=0.5):
        raw_pos = pyautogui.position()
        pos = ClickHelper.__get_absolutely_position__(offset_x, offset_y)
        pyautogui.moveTo(pos)
        pyautogui.scroll(clicks)
        pyautogui.moveTo(raw_pos)
        time.sleep(wait_second)

    @staticmethod
    def exist(pic_path, confidence=0.9):
        pos = pyautogui.locateCenterOnScreen(pic_path, confidence=confidence)
        return pos is not None

    @staticmethod
    def try_return(position='left', wait_second=0.5):
        raw_pos = pyautogui.position()
        if position == 'left':
            ClickHelper.click(55, 970)
        elif position == 'center':
            ClickHelper.click(270, 980)
        pyautogui.moveTo(raw_pos)
        time.sleep(wait_second)
