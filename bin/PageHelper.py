from commons.AutoAdb import AutoAdb


class PageHelper:
    adb = AutoAdb()

    def back(self, nums=1):
        backed_nums = 0
        while backed_nums < nums:
            self.adb.click_position(100, 1800)
            backed_nums = backed_nums + 1

    def go_to_fight_page(self):
        img_list = ['images/page/main-page-fight.png', 'images/page/back.png']
        while True:
            if self.adb.click(*img_list):
                continue
            clicked = self.adb.click('images/page/fight.png')
            if not clicked:
                print('无法到达关卡[战斗]页面')
            return clicked

    def go_to_challenge_page(self):
        img_list = ['images/page/main-page-fight.png', 'images/page/back.png']
        while True:
            if self.adb.click(*img_list):
                continue
            clicked = self.adb.click('images/page/challenge.png')
            if not clicked:
                print('无法到达关卡[挑战]页面')
            return clicked


if __name__ == '__main__':
    result = PageHelper().go_to_fight_page()
    print(result)
