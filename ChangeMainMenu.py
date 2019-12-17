from enum import Enum

from ClickHelper import ClickHelper


class MainMenu(Enum):
    College = 0
    Fighting = 1


class ChangeMainMenu:
    @staticmethod
    def switch(main_menu=MainMenu.College):
        ClickHelper.try_return()

        college_pic = './src/main-switch-college.png'
        fighting_pic = './src/main-switch-fighting.png'

        while True:
            if ClickHelper.exist(college_pic) or ClickHelper.exist(fighting_pic):
                break
            else:
                ClickHelper.try_return()

        if main_menu == MainMenu.College:
            ClickHelper.click_pic(college_pic, fighting_pic)
        else:
            ClickHelper.click_pic(fighting_pic, college_pic)
